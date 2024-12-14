from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, subscriptions

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(subscriptions.router, prefix="/api/subscription", tags=["Subscriptions"])
