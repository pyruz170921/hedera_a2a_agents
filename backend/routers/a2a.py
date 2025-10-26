# backend/routers/a2a.py
from fastapi import APIRouter, Request, HTTPException
from typing import Any

router = APIRouter()

@router.post("/receive")
async def a2a_receive(req: Request):
    """
    Endpoint que actúa como receptor A2A minimal.
    Recibe JSON-RPC 2.0 y procesa métodos de ejemplo.
    """
    payload = await req.json()
    method = payload.get("method")
    params = payload.get("params")
    if not method:
        raise HTTPException(status_code=400, detail="Invalid A2A message")
    # Ejemplo de manejo de propuesta
    if method == "proposal.create":
        proposal = params.get("proposal")
        # Aquí implementar lógica: validar, almacenar, responder o contraoferta
        # Respuesta JSON-RPC de ejemplo: acceptance
        return {"jsonrpc": "2.0", "result": {"status": "accepted", "proposal": proposal}, "id": payload.get("id")}
    # Métodos no implementados
    return {"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found"}, "id": payload.get("id")}
