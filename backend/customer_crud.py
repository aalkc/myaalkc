"""
CRUD operations for customer management.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    """
    Create a new customer in the database.
    
    Args:
        db: Database session
        customer: Customer data to create
        
    Returns:
        Created customer object
        
    Raises:
        IntegrityError: If email already exists
    """
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address
    )
    
    try:
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except IntegrityError as e:
        db.rollback()
        raise e


def get_customer(db: Session, customer_id: int) -> Optional[models.Customer]:
    """
    Get a customer by ID.
    
    Args:
        db: Database session
        customer_id: ID of the customer to retrieve
        
    Returns:
        Customer object if found, None otherwise
    """
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100) -> List[models.Customer]:
    """
    Get a list of customers with pagination.
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        List of customer objects
    """
    return db.query(models.Customer).offset(skip).limit(limit).all()


def get_customer_by_email(db: Session, email: str) -> Optional[models.Customer]:
    """
    Get a customer by email address.
    
    Args:
        db: Database session
        email: Email address to search for
        
    Returns:
        Customer object if found, None otherwise
    """
    return db.query(models.Customer).filter(models.Customer.email == email).first()