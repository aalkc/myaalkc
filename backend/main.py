"""
Main FastAPI application for Amanat Al-Kalima Company ERP API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.customer_router import router as customer_router

# Create FastAPI app instance
app = FastAPI(
    title="Amanat Al-Kalima Company ERP API",
    description="Enterprise Resource Planning API for Amanat Al-Kalima Company",
    version="1.0.0"
)

# Configure CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can be made more specific later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(customer_router)

# Root endpoint
@app.get("/")
async def root():
    """Welcome endpoint for the API."""
    return {"message": "Welcome to Amanat Al-Kalima Company ERP API"}