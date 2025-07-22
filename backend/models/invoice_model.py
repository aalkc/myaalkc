"""
Invoice models for the ZATCA E-Invoicing module.

This module defines the Invoice and InvoiceItem SQLAlchemy models for handling
e-invoicing in the Amanat Al-Kalima Company ERP system according to ZATCA requirements.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Invoice(Base):
    """
    Invoice model for ZATCA E-Invoicing.
    
    Attributes:
        id (int): Primary key identifier for the invoice
        customer_id (int): Foreign key reference to the customer
        invoice_issue_date (datetime): Date when the invoice was issued
        due_date (datetime): Due date for payment
        total_amount (float): Total amount before VAT
        vat_amount (float): VAT amount
        total_amount_with_vat (float): Total amount including VAT
        status (str): Invoice status (e.g., 'Draft', 'Sent', 'Paid')
        items (relationship): Related invoice items
    """
    
    __tablename__ = "invoices"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Customer relationship
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False, index=True)
    
    # Date information
    invoice_issue_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)
    
    # Financial information
    total_amount = Column(Float, nullable=False, default=0.0)
    vat_amount = Column(Float, nullable=False, default=0.0)
    total_amount_with_vat = Column(Float, nullable=False, default=0.0)
    
    # Status information
    status = Column(String(50), nullable=False, default='Draft')
    
    # Relationship to invoice items
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    
    def __repr__(self):
        """String representation of the Invoice object."""
        return f"<Invoice(id={self.id}, customer_id={self.customer_id}, total_amount_with_vat={self.total_amount_with_vat}, status='{self.status}')>"


class InvoiceItem(Base):
    """
    Invoice item model for individual line items within an invoice.
    
    Attributes:
        id (int): Primary key identifier for the invoice item
        invoice_id (int): Foreign key reference to the parent invoice
        item_name (str): Name of the item/service
        quantity (float): Quantity of the item
        unit_price (float): Unit price of the item
        line_total (float): Total amount for this line item
        invoice (relationship): Related invoice
    """
    
    __tablename__ = "invoice_items"
    
    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    
    # Invoice relationship
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False, index=True)
    
    # Item information
    item_name = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False, default=1.0)
    unit_price = Column(Float, nullable=False, default=0.0)
    line_total = Column(Float, nullable=False, default=0.0)
    
    # Relationship to invoice
    invoice = relationship("Invoice", back_populates="items")
    
    def __repr__(self):
        """String representation of the InvoiceItem object."""
        return f"<InvoiceItem(id={self.id}, invoice_id={self.invoice_id}, item_name='{self.item_name}', quantity={self.quantity}, line_total={self.line_total})>"