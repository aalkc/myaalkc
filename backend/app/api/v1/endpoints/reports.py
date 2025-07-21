"""
Reports and analytics endpoints
"""

from typing import Any, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models
from app.api import deps

router = APIRouter()


@router.get("/dashboard")
def get_dashboard_stats(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get dashboard statistics.
    """
    # Get inventory count
    inventory_count = db.query(func.count(models.InventoryItem.id)).scalar()
    
    # Get total inventory value
    inventory_value = db.query(func.sum(
        models.InventoryItem.quantity * models.InventoryItem.unit_price
    )).scalar() or 0
    
    # Get sales count
    sales_count = db.query(func.count(models.SaleOrder.id)).scalar()
    
    # Get purchase orders count
    purchase_count = db.query(func.count(models.PurchaseOrder.id)).scalar()
    
    return {
        "inventory": {
            "total_items": inventory_count,
            "total_value": float(inventory_value)
        },
        "sales": {
            "total_orders": sales_count
        },
        "purchasing": {
            "total_orders": purchase_count
        }
    }


@router.get("/inventory/summary")
def get_inventory_summary(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get inventory summary by category.
    """
    summary = db.query(
        models.InventoryItem.category,
        func.count(models.InventoryItem.id).label('count'),
        func.sum(models.InventoryItem.quantity).label('total_quantity'),
        func.sum(models.InventoryItem.quantity * models.InventoryItem.unit_price).label('total_value')
    ).group_by(models.InventoryItem.category).all()
    
    return [
        {
            "category": item.category,
            "count": item.count,
            "total_quantity": float(item.total_quantity),
            "total_value": float(item.total_value)
        }
        for item in summary
    ]


@router.get("/sales/summary")
def get_sales_summary(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get sales summary by status.
    """
    summary = db.query(
        models.SaleOrder.status,
        func.count(models.SaleOrder.id).label('count'),
        func.sum(models.SaleOrder.total_amount).label('total_amount')
    ).group_by(models.SaleOrder.status).all()
    
    return [
        {
            "status": item.status,
            "count": item.count,
            "total_amount": float(item.total_amount)
        }
        for item in summary
    ]