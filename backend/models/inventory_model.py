"""
Inventory model for the Inventory Management module.

This module defines the Inventory SQLAlchemy model for tracking inventory items
in the Amanat Al-Kalima Company ERP system.
"""

from sqlalchemy import Column, Integer, String, Float
from database import Base


class Inventory(Base):
    """
    Inventory model for tracking inventory items.
    
    Attributes:
        id (int): Primary key identifier for the inventory item
        item_name (str): Name of the inventory item
        item_type (str): Type/category of the inventory item
        quantity (float): Current quantity of the item in stock
        weight (float): Weight of the item
        unit (str): Unit of measurement (e.g., 'kg', 'ton', 'lbs')
        purchase_price (float): Purchase price of the item
        location (str): Storage location of the item
    """
    
    __tablename__ = "inventory"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Item information
    item_name = Column(String(255), nullable=False, index=True)
    item_type = Column(String(100), nullable=False)
    
    # Quantity and measurement
    quantity = Column(Float, nullable=False, default=0.0)
    weight = Column(Float, nullable=False, default=0.0)
    unit = Column(String(20), nullable=False, default='kg')
    
    # Financial information
    purchase_price = Column(Float, nullable=False, default=0.0)
    
    # Location information
    location = Column(String(255), nullable=False)
    
    def __repr__(self):
        """String representation of the Inventory object."""
        return f"<Inventory(id={self.id}, item_name='{self.item_name}', quantity={self.quantity}, location='{self.location}')>"