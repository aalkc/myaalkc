"""
Sales management endpoints
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.SaleOrder])
def read_sale_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve sale orders.
    """
    orders = db.query(models.SaleOrder).offset(skip).limit(limit).all()
    return orders


@router.post("/", response_model=schemas.SaleOrder)
def create_sale_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.SaleOrderCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new sale order.
    """
    order = models.SaleOrder(**order_in.dict(), created_by=current_user.id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/{order_id}", response_model=schemas.SaleOrder)
def read_sale_order(
    *,
    db: Session = Depends(deps.get_db),
    order_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get sale order by ID.
    """
    order = db.query(models.SaleOrder).filter(models.SaleOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{order_id}/status")
def update_sale_order_status(
    *,
    db: Session = Depends(deps.get_db),
    order_id: int,
    status: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update sale order status.
    """
    order = db.query(models.SaleOrder).filter(models.SaleOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = status
    db.add(order)
    db.commit()
    db.refresh(order)
    return {"message": "Status updated successfully", "order": order}