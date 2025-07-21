"""
Main FastAPI application.
"""

from fastapi import FastAPI
from .database import init_db, create_tables
from .routers import customer_router

# Initialize FastAPI app
app = FastAPI(
    title="Customer Management API",
    description="A simple API for managing customers",
    version="1.0.0",
)

# Include routers
app.include_router(customer_router.router)

@app.on_event("startup")
async def startup_event():
    """
    Initialize database on startup.
    """
    init_db()
    create_tables()

@app.get("/")
def read_root():
    """
    Root endpoint.
    """
    return {"message": "Customer Management API", "version": "1.0.0"}