"""
SQLAlchemy models for the database entities.

This module defines the database models using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class Customer(Base):
    """
    Customer model for storing customer information.
    
    Attributes:
        id (int): Primary key, auto-incrementing customer ID
        name (str): Customer name (required)
        email (str): Customer email address (unique, required)
        phone (str): Customer phone number (optional)
        created_at (datetime): Timestamp when customer was created
        updated_at (datetime): Timestamp when customer was last updated
    """
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"