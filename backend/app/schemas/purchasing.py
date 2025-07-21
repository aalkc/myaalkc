"""
Purchasing schemas
"""

from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, EmailStr


class SupplierBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = "Saudi Arabia"
    tax_id: Optional[str] = None
    payment_terms: Optional[str] = None


class SupplierCreate(SupplierBase):
    name: str
    email: EmailStr


class Supplier(SupplierBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PurchaseOrderBase(BaseModel):
    order_number: Optional[str] = None
    supplier_id: Optional[int] = None
    status: Optional[str] = "pending"
    total_amount: Optional[Decimal] = None
    currency: Optional[str] = "SAR"
    tax_amount: Optional[Decimal] = None
    discount_amount: Optional[Decimal] = None
    notes: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None


class PurchaseOrderCreate(PurchaseOrderBase):
    order_number: str
    supplier_id: int
    total_amount: Decimal


class PurchaseOrderUpdate(PurchaseOrderBase):
    pass


class PurchaseOrderInDBBase(PurchaseOrderBase):
    id: Optional[int] = None
    order_date: Optional[datetime] = None
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class PurchaseOrder(PurchaseOrderInDBBase):
    supplier: Optional[Supplier] = None


class PurchaseOrderInDB(PurchaseOrderInDBBase):
    pass