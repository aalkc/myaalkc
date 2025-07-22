"""
Inventory router for handling inventory-related API endpoints.

This module provides RESTful API endpoints for inventory management
including CRUD operations for inventory items.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from crud.inventory_crud import (
    create_inventory_item,
    get_inventory_item_by_id,
    get_all_inventory_items,
    update_inventory_item,
    delete_inventory_item
)
from schemas.inventory_schema import (
    Inventory,
    InventoryCreate,
    InventoryUpdate
)

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"]
)


@router.post("/", response_model=Inventory, status_code=status.HTTP_201_CREATED)
async def create_new_inventory_item(
    inventory_item: InventoryCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new inventory item.
    
    Args:
        inventory_item (InventoryCreate): Inventory item data to create
        db (Session): Database session dependency
        
    Returns:
        Inventory: The created inventory item
        
    Raises:
        HTTPException: If creation fails
    """
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
    """
    Retrieve all inventory items with pagination.
    
    Args:
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.
        db (Session): Database session dependency
        
    Returns:
        List[Inventory]: List of inventory items
        
    Raises:
        HTTPException: If retrieval fails
    """
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
    """
    Retrieve a single inventory item by ID.
    
    Args:
        item_id (int): ID of the inventory item to retrieve
        db (Session): Database session dependency
        
    Returns:
        Inventory: The inventory item if found
        
    Raises:
        HTTPException: If item not found or retrieval fails
    """
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
async def update_existing_inventory_item(
    item_id: int,
    inventory_update: InventoryUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing inventory item.
    
    Args:
        item_id (int): ID of the inventory item to update
        inventory_update (InventoryUpdate): Updated inventory item data
        db (Session): Database session dependency
        
    Returns:
        Inventory: The updated inventory item
        
    Raises:
        HTTPException: If item not found or update fails
    """
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
async def delete_inventory_item_by_id(
    item_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an inventory item by ID.
    
    Args:
        item_id (int): ID of the inventory item to delete
        db (Session): Database session dependency
        
    Raises:
        HTTPException: If item not found or deletion fails
    """
    try:
        deleted = delete_inventory_item(db=db, item_id=item_id)
        if not deleted:
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