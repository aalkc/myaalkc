"""
Inventory schemas
"""

from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel


class InventoryItemBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    sku: Optional[str] = None
    quantity: Optional[Decimal] = None
    unit: Optional[str] = None
    unit_price: Optional[Decimal] = None
    location: Optional[str] = None
    minimum_stock: Optional[Decimal] = None


class InventoryItemCreate(InventoryItemBase):
    name: str
    category: str
    sku: str
    quantity: Decimal
    unit: str
    unit_price: Decimal


class InventoryItemUpdate(InventoryItemBase):
    pass


class InventoryItemInDBBase(InventoryItemBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class InventoryItem(InventoryItemInDBBase):
    pass


class InventoryItemInDB(InventoryItemInDBBase):
    pass