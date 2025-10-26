# backend/agents/a2a_client.py
"""
Cliente simple A2A (JSON-RPC 2.0 over HTTP).
Se puede reemplazar por el SDK A2A real si está disponible.
"""
import requests
from typing import Any

def send_a2a_message(target_url: str, method: str, params: dict, req_id: int = 1, timeout: int = 15) -> Any:
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": req_id
    }
    headers = {"Content-Type": "application/json"}
    resp = requests.post(target_url, json=payload, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.json()
