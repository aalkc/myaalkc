"""
CRUD operations package for database entities.

This package contains modules for performing Create, Read, Update, and Delete
operations on various database models.
"""

from .customer_crud import create_customer, get_customer, get_all_customers

__all__ = [
    "create_customer",
    "get_customer", 
    "get_all_customers"
]