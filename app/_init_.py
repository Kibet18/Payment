from fastapi import FastAPI
from app.database import Base, engine
from app.routes import subscriptions, payments

# Initialize the FastAPI application
app = FastAPI(
    title="Business Directory API",
    description="API for managing subscriptions, businesses, and payments",
    version="1.0.0",
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(subscriptions.router, prefix="/api/subscription", tags=["Subscriptions"])
app.include_router(payments.router, prefix="/api/payment", tags=["Payments"])
