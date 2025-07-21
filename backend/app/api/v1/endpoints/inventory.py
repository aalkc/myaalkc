"""
Inventory management endpoints
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.InventoryItem])
def read_inventory_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve inventory items.
    """
    items = db.query(models.InventoryItem).offset(skip).limit(limit).all()
    return items


@router.post("/", response_model=schemas.InventoryItem)
def create_inventory_item(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.InventoryItemCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new inventory item.
    """
    item = models.InventoryItem(**item_in.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/{item_id}", response_model=schemas.InventoryItem)
def read_inventory_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get inventory item by ID.
    """
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.InventoryItem)
def update_inventory_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    item_in: schemas.InventoryItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an inventory item.
    """
    item = db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    update_data = item_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
    
    db.add(item)
    db.commit()
    db.refresh(item)
    return item