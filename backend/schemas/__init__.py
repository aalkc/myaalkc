"""
Schemas package for Pydantic data validation and serialization.

This package contains all the Pydantic schemas used throughout the 
Amanat Al-Kalima Company ERP API for request/response validation.
"""

from .inventory_schema import InventoryCreate, InventoryUpdate, Inventory
from .invoice_schema import (
    InvoiceItemBase,
    InvoiceItemCreate,
    InvoiceItem,
    InvoiceBase,
    InvoiceCreate,
    Invoice
)

__all__ = [
    # Inventory schemas
    "InventoryCreate",
    "InventoryUpdate", 
    "Inventory",
    # Invoice schemas
    "InvoiceItemBase",
    "InvoiceItemCreate",
    "InvoiceItem",
    "InvoiceBase",
    "InvoiceCreate",
    "Invoice",
]