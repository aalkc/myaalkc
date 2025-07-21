"""
Sales schemas
"""

from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = "Saudi Arabia"
    tax_id: Optional[str] = None


class CustomerCreate(CustomerBase):
    name: str
    email: EmailStr


class Customer(CustomerBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class SaleOrderBase(BaseModel):
    order_number: Optional[str] = None
    customer_id: Optional[int] = None
    status: Optional[str] = "pending"
    total_amount: Optional[Decimal] = None
    currency: Optional[str] = "SAR"
    tax_amount: Optional[Decimal] = None
    discount_amount: Optional[Decimal] = None
    notes: Optional[str] = None
    delivery_date: Optional[datetime] = None


class SaleOrderCreate(SaleOrderBase):
    order_number: str
    customer_id: int
    total_amount: Decimal


class SaleOrderUpdate(SaleOrderBase):
    pass


class SaleOrderInDBBase(SaleOrderBase):
    id: Optional[int] = None
    order_date: Optional[datetime] = None
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class SaleOrder(SaleOrderInDBBase):
    customer: Optional[Customer] = None


class SaleOrderInDB(SaleOrderInDBBase):
    pass