"""
Schemas package for myaalkc backend.

This package contains Pydantic schemas for data validation and serialization.
"""

from .customer_schema import Customer, CustomerCreate

__all__ = ["Customer", "CustomerCreate"]