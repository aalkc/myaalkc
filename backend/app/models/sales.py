"""
Sales models
"""

from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    address = Column(String)
    city = Column(String)
    country = Column(String, default="Saudi Arabia")
    tax_id = Column(String)  # VAT/Tax identification number
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    sale_orders = relationship("SaleOrder", back_populates="customer")


class SaleOrder(Base):
    __tablename__ = "sale_orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(String, default="pending")  # pending, confirmed, shipped, delivered, cancelled
    total_amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String, default="SAR")  # Saudi Riyal
    tax_amount = Column(Numeric(12, 2), default=0)
    discount_amount = Column(Numeric(12, 2), default=0)
    notes = Column(String)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    delivery_date = Column(DateTime(timezone=True))
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    customer = relationship("Customer", back_populates="sale_orders")
    creator = relationship("User", back_populates="sale_orders")