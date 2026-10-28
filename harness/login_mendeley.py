"""Launch upstream OAuth with loopback, state validation and safe failures.

Run interactively yourself. Never pass secrets as command-line arguments.
This compatibility wrapper is pinned to mendeley-mcp 0.8.0.
"""
from __future__ import annotations

import secrets
import socketserver
from importlib.metadata import version
from urllib.parse import parse_qs, urlparse
from unittest.mock import patch

import click
import keyring
from mendeley_mcp import auth


def valid_callback(path: str, expected_state: str) -> bool:
    parsed = urlparse(path)
    values = parse_qs(parsed.query)
    states = values.get("state", [])
    return (parsed.path == "/callback" and len(states) == 1
            and secrets.compare_digest(states[0], expected_state))


def main() -> None:
    if version("mendeley-mcp") != "0.8.0":
        raise SystemExit("Unsupported package version; review wrapper before login.")
    if type(keyring.get_keyring()).__module__ != "keyring.backends.Windows":
        raise SystemExit("Windows keyring unavailable; login stopped without file fallback.")

    expected_state = secrets.token_urlsafe(32)
    upstream_exchange = auth.exchange_code_for_tokens

    class Callback(auth.OAuthCallbackHandler):
        def do_GET(self) -> None:
            if not valid_callback(self.path, expected_state):
                self.send_error(400, "Invalid OAuth callback")
                return
            values = parse_qs(urlparse(self.path).query)
            if len(values.get("code", [])) != 1 or "error" in values:
                self.send_error(400, "Authorization not completed")
                return
            super().do_GET()

    class LoopbackServer(socketserver.TCPServer):
        def __init__(self, address: tuple[str, int], handler: type) -> None:
            super().__init__(("127.0.0.1", address[1]), handler)
            self.timeout = 300

    def exchange_safely(*args: object, **kwargs: object) -> dict:
        try:
            return upstream_exchange(*args, **kwargs)
        except Exception:
            raise click.ClickException("OAuth token exchange failed; credentials redacted.") from None

    with patch.object(auth, "OAuthCallbackHandler", Callback), \
         patch.object(auth.socketserver, "TCPServer", LoopbackServer), \
         patch.object(auth.secrets, "token_urlsafe", return_value=expected_state), \
         patch.object(auth, "exchange_code_for_tokens", exchange_safely):
        try:
            auth.cli(args=["login"], prog_name="Mendeley login")
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            raise SystemExit("Login/storage failed; details redacted. No secrets printed.") from None


if __name__ == "__main__":
    main()
