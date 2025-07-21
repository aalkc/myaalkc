"""
Purchasing management endpoints
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.PurchaseOrder])
def read_purchase_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve purchase orders.
    """
    orders = db.query(models.PurchaseOrder).offset(skip).limit(limit).all()
    return orders


@router.post("/", response_model=schemas.PurchaseOrder)
def create_purchase_order(
    *,
    db: Session = Depends(deps.get_db),
    order_in: schemas.PurchaseOrderCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new purchase order.
    """
    order = models.PurchaseOrder(**order_in.dict(), created_by=current_user.id)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/{order_id}", response_model=schemas.PurchaseOrder)
def read_purchase_order(
    *,
    db: Session = Depends(deps.get_db),
    order_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get purchase order by ID.
    """
    order = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/suppliers/", response_model=List[schemas.Supplier])
def read_suppliers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve suppliers.
    """
    suppliers = db.query(models.Supplier).offset(skip).limit(limit).all()
    return suppliers


@router.post("/suppliers/", response_model=schemas.Supplier)
def create_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_in: schemas.SupplierCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new supplier.
    """
    supplier = models.Supplier(**supplier_in.dict())
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier