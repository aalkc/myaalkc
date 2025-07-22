"""
Inventory router for handling inventory-related API endpoints.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.inventory_schema import Inventory, InventoryCreate, InventoryUpdate
from crud.inventory_crud import (
    create_inventory_item,
    get_inventory_item_by_id,
    get_all_inventory_items,
    update_inventory_item,
    delete_inventory_item
)

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)

@router.post("/", response_model=Inventory, status_code=status.HTTP_201_CREATED)
async def create_inventory(
    inventory_item: InventoryCreate,
    db: Session = Depends(get_db)
):
    """Create a new inventory item."""
    try:
        return create_inventory_item(db=db, inventory_item=inventory_item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create inventory item: {str(e)}"
        )

@router.get("/", response_model=List[Inventory])
async def get_inventory_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all inventory items with optional pagination."""
    try:
        return get_all_inventory_items(db=db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve inventory items: {str(e)}"
        )

@router.get("/{item_id}", response_model=Inventory)
async def get_inventory_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific inventory item by ID."""
    try:
        inventory_item = get_inventory_item_by_id(db=db, item_id=item_id)
        if inventory_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Inventory item with ID {item_id} not found"
            )
        return inventory_item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve inventory item: {str(e)}"
        )

@router.put("/{item_id}", response_model=Inventory)
async def update_inventory(
    item_id: int,
    inventory_update: InventoryUpdate,
    db: Session = Depends(get_db)
):
    """Update an existing inventory item."""
    try:
        updated_item = update_inventory_item(db=db, item_id=item_id, inventory_update=inventory_update)
        if updated_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Inventory item with ID {item_id} not found"
            )
        return updated_item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update inventory item: {str(e)}"
        )

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory(
    item_id: int,
    db: Session = Depends(get_db)
):
    """Delete an inventory item."""
    try:
        success = delete_inventory_item(db=db, item_id=item_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Inventory item with ID {item_id} not found"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete inventory item: {str(e)}"
        )