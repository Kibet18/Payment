from fastapi import APIRouter, Depends
from app.auth import get_current_user, require_role

router = APIRouter()

@router.get("/my-subscriptions")
def list_my_subscriptions(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome {current_user['email']}! Here are your subscriptions."}

@router.post("/create", dependencies=[Depends(require_role("vendor"))])
def create_subscription():
    return {"message": "Subscription created successfully!"}
