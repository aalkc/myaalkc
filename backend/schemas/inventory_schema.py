"""
Inventory schemas for the Inventory Management module.

This module defines Pydantic schemas for inventory-related operations
including creation, updates, and response models.
"""

from typing import Optional
from pydantic import BaseModel, Field


class InventoryCreate(BaseModel):
    """
    Schema for creating a new inventory item.
    
    This schema defines the required and optional fields when creating
    a new inventory item in the system.
    """
    
    item_name: str = Field(..., min_length=1, max_length=255, description="Name of the inventory item")
    item_type: str = Field(..., min_length=1, max_length=100, description="Type/category of the inventory item")
    quantity: float = Field(default=0.0, ge=0.0, description="Current quantity of the item in stock")
    weight: float = Field(default=0.0, ge=0.0, description="Weight of the item")
    unit: str = Field(default="kg", min_length=1, max_length=20, description="Unit of measurement (e.g., 'kg', 'ton', 'lbs')")
    purchase_price: float = Field(default=0.0, ge=0.0, description="Purchase price of the item")
    location: str = Field(..., min_length=1, max_length=255, description="Storage location of the item")


class InventoryUpdate(BaseModel):
    """
    Schema for updating an existing inventory item.
    
    All fields are optional to allow partial updates of inventory items.
    """
    
    item_name: Optional[str] = Field(None, min_length=1, max_length=255, description="Name of the inventory item")
    item_type: Optional[str] = Field(None, min_length=1, max_length=100, description="Type/category of the inventory item")
    quantity: Optional[float] = Field(None, ge=0.0, description="Current quantity of the item in stock")
    weight: Optional[float] = Field(None, ge=0.0, description="Weight of the item")
    unit: Optional[str] = Field(None, min_length=1, max_length=20, description="Unit of measurement (e.g., 'kg', 'ton', 'lbs')")
    purchase_price: Optional[float] = Field(None, ge=0.0, description="Purchase price of the item")
    location: Optional[str] = Field(None, min_length=1, max_length=255, description="Storage location of the item")


class Inventory(BaseModel):
    """
    Schema for inventory item response.
    
    This schema represents the full inventory item as returned by the API,
    including all fields from the database model.
    """
    
    id: int = Field(..., description="Primary key identifier for the inventory item")
    item_name: str = Field(..., description="Name of the inventory item")
    item_type: str = Field(..., description="Type/category of the inventory item")
    quantity: float = Field(..., description="Current quantity of the item in stock")
    weight: float = Field(..., description="Weight of the item")
    unit: str = Field(..., description="Unit of measurement (e.g., 'kg', 'ton', 'lbs')")
    purchase_price: float = Field(..., description="Purchase price of the item")
    location: str = Field(..., description="Storage location of the item")
    
    class Config:
        """Pydantic configuration for the Inventory schema."""
        from_attributes = True  # Enables compatibility with SQLAlchemy models