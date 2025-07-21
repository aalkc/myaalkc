"""
Main API router for v1
"""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, inventory, purchasing, reports, sales

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
api_router.include_router(sales.router, prefix="/sales", tags=["sales"])
api_router.include_router(purchasing.router, prefix="/purchasing", tags=["purchasing"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])