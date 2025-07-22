"""
Invoice schemas for the ZATCA E-Invoicing module.

This module defines Pydantic schemas for invoice-related operations
including creation, updates, and response models for both invoices and invoice items.
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class InvoiceItemBase(BaseModel):
    """
    Base schema for invoice items.
    
    Contains the common fields shared between different invoice item schemas.
    """
    
    item_name: str = Field(..., min_length=1, max_length=255, description="Name of the item/service")
    quantity: float = Field(default=1.0, gt=0.0, description="Quantity of the item")
    unit_price: float = Field(default=0.0, ge=0.0, description="Unit price of the item")


class InvoiceItemCreate(InvoiceItemBase):
    """
    Schema for creating a new invoice item.
    
    This schema inherits from InvoiceItemBase and includes all necessary fields
    for creating an invoice item. The line_total will be calculated automatically.
    """
    pass  # All fields inherited from InvoiceItemBase


class InvoiceItem(InvoiceItemBase):
    """
    Schema for invoice item response.
    
    This schema represents the complete invoice item as returned by the API,
    including the calculated line_total and database identifiers.
    """
    
    id: int = Field(..., description="Primary key identifier for the invoice item")
    invoice_id: int = Field(..., description="Foreign key reference to the parent invoice")
    line_total: float = Field(..., description="Total amount for this line item (quantity * unit_price)")
    
    class Config:
        """Pydantic configuration for the InvoiceItem schema."""
        from_attributes = True  # Enables compatibility with SQLAlchemy models


class InvoiceBase(BaseModel):
    """
    Base schema for invoices.
    
    Contains the common fields shared between different invoice schemas.
    """
    
    customer_id: int = Field(..., gt=0, description="Foreign key reference to the customer")
    invoice_issue_date: datetime = Field(..., description="Date when the invoice was issued")
    due_date: datetime = Field(..., description="Due date for payment")
    status: str = Field(default='Draft', min_length=1, max_length=50, description="Invoice status (e.g., 'Draft', 'Sent', 'Paid')")


class InvoiceCreate(InvoiceBase):
    """
    Schema for creating a new invoice with its items.
    
    This schema allows creating a complete invoice with all its line items
    in a single API call. The financial totals will be calculated automatically.
    """
    
    items: List[InvoiceItemCreate] = Field(default=[], description="List of invoice items")


class Invoice(InvoiceBase):
    """
    Schema for invoice response.
    
    This schema represents the complete invoice as returned by the API,
    including all calculated financial totals and the list of invoice items.
    """
    
    id: int = Field(..., description="Primary key identifier for the invoice")
    total_amount: float = Field(..., description="Total amount before VAT")
    vat_amount: float = Field(..., description="VAT amount")
    total_amount_with_vat: float = Field(..., description="Total amount including VAT")
    items: List[InvoiceItem] = Field(default=[], description="List of invoice items")
    
    class Config:
        """Pydantic configuration for the Invoice schema."""
        from_attributes = True  # Enables compatibility with SQLAlchemy models