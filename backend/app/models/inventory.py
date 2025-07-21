"""
Inventory models
"""

from sqlalchemy import Column, Integer, String, Numeric, DateTime, func

from app.core.database import Base


class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    category = Column(String, nullable=False, index=True)  # e.g., "Aluminum", "Copper", "Steel"
    sku = Column(String, unique=True, index=True)
    quantity = Column(Numeric(10, 2), nullable=False, default=0)
    unit = Column(String, nullable=False)  # e.g., "kg", "ton", "pieces"
    unit_price = Column(Numeric(10, 2), nullable=False)
    location = Column(String)  # Storage location
    minimum_stock = Column(Numeric(10, 2), default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())