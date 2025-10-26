# backend/routers/payments.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx

router = APIRouter()

# URL del servicio Node.js (bridge)
BRIDGE_URL = "http://localhost:4000"  # Cambia el puerto si tu bridge usa otro

class PaymentIntent(BaseModel):
    payer: str
    payee: str
    amount: int
    currency: str  # "HTS" o "ERC20"
    token_id: str | None = None
    contract: str | None = None


@router.post("/create")
async def create_payment(intent: PaymentIntent):
    """
    Endpoint que recibe un PaymentIntent (AP2-like) y orquesta la liquidación vía bridge.
    """
    try:
        async with httpx.AsyncClient() as client:
            if intent.currency.upper() == "HTS":
                if not intent.token_id:
                    raise HTTPException(status_code=400, detail="Falta token_id para HTS")
                response = await client.post(
                    f"{BRIDGE_URL}/transfer/hts",
                    json={
                        "payer": intent.payer,
                        "payee": intent.payee,
                        "amount": intent.amount,
                        "token_id": intent.token_id,
                    },
                )

            elif intent.currency.upper() == "ERC20":
                if not intent.contract:
                    raise HTTPException(status_code=400, detail="Falta contract para ERC20")
                response = await client.post(
                    f"{BRIDGE_URL}/transfer/erc20",
                    json={
                        "payer": intent.payer,
                        "payee": intent.payee,
                        "amount": intent.amount,
                        "contract": intent.contract,
                    },
                )

            else:
                raise HTTPException(status_code=400, detail="Moneda no soportada")

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return {"status": "ok", "tx": response.json()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
