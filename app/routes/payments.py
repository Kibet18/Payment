from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class WebhookPayload(BaseModel):
    event_type: str
    data: dict

@router.post("/webhook")
def payment_webhook(payload: WebhookPayload):
    if payload.event_type == "payment_failed":
        # Handle failed payment logic (e.g., notify the vendor)
        return {"message": "Payment failure handled"}
    elif payload.event_type == "payment_success":
        # Handle success logic
        return {"message": "Payment success handled"}
    else:
        raise HTTPException(status_code=400, detail="Unknown event type")
