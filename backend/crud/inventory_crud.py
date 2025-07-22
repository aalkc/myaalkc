"""
Inventory CRUD operations for the Inventory Management module.

This module provides CRUD (Create, Read, Update, Delete) operations
for inventory items in the Amanat Al-Kalima Company ERP system.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.inventory_model import Inventory
from schemas.inventory_schema import InventoryCreate, InventoryUpdate


def create_inventory_item(db: Session, inventory_item: InventoryCreate) -> Inventory:
    """
    Create a new inventory item in the database.
    
    Args:
        db (Session): Database session
        inventory_item (InventoryCreate): Inventory item data to create
        
    Returns:
        Inventory: The created inventory item
        
    Raises:
        SQLAlchemyError: If database operation fails
    """
    try:
        # Create new inventory item instance
        db_inventory = Inventory(
            item_name=inventory_item.item_name,
            item_type=inventory_item.item_type,
            quantity=inventory_item.quantity,
            weight=inventory_item.weight,
            unit=inventory_item.unit,
            purchase_price=inventory_item.purchase_price,
            location=inventory_item.location
        )
        
        # Add to database session
        db.add(db_inventory)
        db.commit()
        db.refresh(db_inventory)
        
        return db_inventory
        
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def get_inventory_item_by_id(db: Session, item_id: int) -> Optional[Inventory]:
    """
    Retrieve an inventory item by its ID.
    
    Args:
        db (Session): Database session
        item_id (int): ID of the inventory item to retrieve
        
    Returns:
        Optional[Inventory]: The inventory item if found, None otherwise
    """
    try:
        return db.query(Inventory).filter(Inventory.id == item_id).first()
    except SQLAlchemyError as e:
        raise e


def get_all_inventory_items(db: Session, skip: int = 0, limit: int = 100) -> List[Inventory]:
    """
    Retrieve all inventory items with optional pagination.
    
    Args:
        db (Session): Database session
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 100.
        
    Returns:
        List[Inventory]: List of inventory items
    """
    try:
        return db.query(Inventory).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        raise e


def update_inventory_item(db: Session, item_id: int, inventory_update: InventoryUpdate) -> Optional[Inventory]:
    """
    Update an existing inventory item.
    
    Args:
        db (Session): Database session
        item_id (int): ID of the inventory item to update
        inventory_update (InventoryUpdate): Updated inventory item data
        
    Returns:
        Optional[Inventory]: The updated inventory item if found, None otherwise
        
    Raises:
        SQLAlchemyError: If database operation fails
    """
    try:
        # Get the existing inventory item
        db_inventory = db.query(Inventory).filter(Inventory.id == item_id).first()
        
        if not db_inventory:
            return None
            
        # Update only the fields that are provided (not None)
        update_data = inventory_update.model_dump(exclude_unset=True)
        
        for field, value in update_data.items():
            if hasattr(db_inventory, field):
                setattr(db_inventory, field, value)
        
        db.commit()
        db.refresh(db_inventory)
        
        return db_inventory
        
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_inventory_item(db: Session, item_id: int) -> bool:
    """
    Delete an inventory item by its ID.
    
    Args:
        db (Session): Database session
        item_id (int): ID of the inventory item to delete
        
    Returns:
        bool: True if the item was deleted, False if not found
        
    Raises:
        SQLAlchemyError: If database operation fails
    """
    try:
        # Get the existing inventory item
        db_inventory = db.query(Inventory).filter(Inventory.id == item_id).first()
        
        if not db_inventory:
            return False
            
        # Delete the item
        db.delete(db_inventory)
        db.commit()
        
        return True
        
    except SQLAlchemyError as e:
        db.rollback()
        raise e