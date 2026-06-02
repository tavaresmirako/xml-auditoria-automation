from typing import Any

import requests


class APIClient:
    """HTTP client used to send processed XML payloads to an external API."""

    def __init__(self, endpoint: str, token: str | None = None):
        self.endpoint = endpoint
        self.token = token

    def send_audit_payload(self, payload: dict[str, Any]) -> dict[str, Any]:
        headers = {"Content-Type": "application/json"}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.post(
            self.endpoint,
            json=payload,
            headers=headers,
            timeout=30,
        )

        if response.status_code not in [200, 201]:
            raise RuntimeError(
                f"API request failed: {response.status_code} - {response.text}"
            )

        return response.json()
