"""
Customer router for handling customer-related API endpoints.
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.get("/")
async def get_customers():
    """Get all customers."""
    return {"message": "Customer endpoints will be implemented here"}