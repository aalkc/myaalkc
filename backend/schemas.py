"""
Pydantic schemas for API request and response models.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    """
    Base schema for customer data.
    """
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None


class CustomerCreate(CustomerBase):
    """
    Schema for creating a new customer.
    """
    pass


class CustomerResponse(CustomerBase):
    """
    Schema for customer response data.
    """
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)