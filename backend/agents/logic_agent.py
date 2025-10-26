# backend/agents/logic_agent.py
"""
Lógica de ejemplo para un agente local que crea una propuesta A2A y procesa respuestas.
En producción esto sería una clase más compleja (LLM, memoria, capacidades).
"""
from .a2a_client import send_a2a_message

def propose_service(agent_card_url: str, service_desc: dict):
    """
    Construye y envía una propuesta A2A a otro agente.
    service_desc ejemplo: {"item":"hotel","date":"2025-11-10","price":100}
    """
    method = "proposal.create"
    params = {"proposal": service_desc}
    return send_a2a_message(agent_card_url, method, params)
.
