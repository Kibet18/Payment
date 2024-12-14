from pydantic import BaseModel
from typing import Optional

class SubscriptionCreate(BaseModel):
    business_id: int
    stripe_token: str

class PaymentResponse(BaseModel):
    message: str
    transaction_id: Optional[int] = None
