from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from ..models.invoice import Invoice
from ..schemas.invoice import InvoiceCreate, InvoiceUpdate


def create_invoice(db: Session, invoice_in: InvoiceCreate) -> Invoice:
    """
    Create a new invoice in the database.
    
    Args:
        db: Database session
        invoice_in: Invoice data
        
    Returns:
        The created invoice with ID
    """
    # Create invoice object with the main details from schema
    invoice = Invoice(
        customer_id=invoice_in.customer_id,
        issue_date=invoice_in.issue_date,
        due_date=invoice_in.due_date,
        status=invoice_in.status,
        amount_total=invoice_in.amount_total,
        amount_due=invoice_in.amount_due,
        notes=invoice_in.notes if hasattr(invoice_in, "notes") else None,
        payment_terms=invoice_in.payment_terms if hasattr(invoice_in, "payment_terms") else None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    # Add to database
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    
    return invoice


def get_invoice(db: Session, invoice_id: int) -> Optional[Invoice]:
    """
    Get an invoice by ID.
    
    Args:
        db: Database session
        invoice_id: ID of the invoice to retrieve
        
    Returns:
        Invoice if found, None otherwise
    """
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()


def get_invoices(db: Session, skip: int = 0, limit: int = 100) -> List[Invoice]:
    """
    Get all invoices with pagination.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of invoices
    """
    return db.query(Invoice).offset(skip).limit(limit).all()


def get_customer_invoices(db: Session, customer_id: int) -> List[Invoice]:
    """
    Get all invoices for a specific customer.
    
    Args:
        db: Database session
        customer_id: ID of the customer
        
    Returns:
        List of invoices for the customer
    """
    return db.query(Invoice).filter(Invoice.customer_id == customer_id).all()


def update_invoice(db: Session, invoice_id: int, invoice_in: InvoiceUpdate) -> Optional[Invoice]:
    """
    Update an existing invoice.
    
    Args:
        db: Database session
        invoice_id: ID of the invoice to update
        invoice_in: New invoice data
        
    Returns:
        Updated invoice if found, None otherwise
    """
    invoice = get_invoice(db, invoice_id)
    if invoice:
        update_data = invoice_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(invoice, field, value)
        
        invoice.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(invoice)
        
    return invoice


def delete_invoice(db: Session, invoice_id: int) -> bool:
    """
    Delete an invoice.
    
    Args:
        db: Database session
        invoice_id: ID of the invoice to delete
        
    Returns:
        True if invoice was deleted, False otherwise
    """
    invoice = get_invoice(db, invoice_id)
    if invoice:
        db.delete(invoice)
        db.commit()
        return True
    return False
