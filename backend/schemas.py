"""
Pydantic schemas for request/response data validation.

This module defines the data schemas used for API requests and responses
using Pydantic for validation and serialization.
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class CustomerBase(BaseModel):
    """Base customer schema with common attributes."""
    name: str = Field(..., min_length=1, max_length=100, description="Customer name")
    email: str = Field(..., description="Customer email address")
    phone: Optional[str] = Field(None, max_length=20, description="Customer phone number")


class CustomerCreate(CustomerBase):
    """Schema for creating a new customer."""
    pass


class CustomerUpdate(CustomerBase):
    """Schema for updating customer information."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)


class CustomerResponse(CustomerBase):
    """Schema for customer response data."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True