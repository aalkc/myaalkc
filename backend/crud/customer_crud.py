"""
Customer CRUD operations for managing customer data in the database.

This module provides functions to create, read, update, and delete customer records
using SQLAlchemy ORM and database sessions.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

from ..models import Customer
from ..schemas import CustomerCreate

# Set up logging
logger = logging.getLogger(__name__)

def create_customer(db: Session, customer_data: CustomerCreate) -> Optional[Customer]:
    """
    Create a new customer in the database.
    
    Args:
        db (Session): Database session
        customer_data (CustomerCreate): CustomerCreate schema object containing customer data
        
    Returns:
        Customer: The created customer object, or None if creation failed
        
    Raises:
        SQLAlchemyError: If there's an error during database operation
    """
    try:
        # Create new customer instance from schema data
        db_customer = Customer(**customer_data.model_dump())
        
        # Add to session and commit
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        
        logger.info(f"Successfully created customer with ID: {db_customer.id}")
        return db_customer
        
    except SQLAlchemyError as e:
        logger.error(f"Error creating customer: {e}")
        db.rollback()
        raise
    except Exception as e:
        logger.error(f"Unexpected error creating customer: {e}")
        db.rollback()
        return None


def get_customer(db: Session, customer_id: int) -> Optional[Customer]:
    """
    Retrieve a specific customer by ID.
    
    Args:
        db (Session): Database session
        customer_id (int): The ID of the customer to retrieve
        
    Returns:
        Customer: The customer object if found, None otherwise
    """
    try:
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        
        if customer:
            logger.info(f"Successfully retrieved customer with ID: {customer_id}")
        else:
            logger.warning(f"Customer with ID {customer_id} not found")
            
        return customer
        
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving customer with ID {customer_id}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error retrieving customer: {e}")
        return None


def get_all_customers(db: Session) -> List[Customer]:
    """
    Retrieve a list of all customers from the database.
    
    Args:
        db (Session): Database session
        
    Returns:
        List[Customer]: List of all customer objects
    """
    try:
        customers = db.query(Customer).all()
        
        logger.info(f"Successfully retrieved {len(customers)} customers")
        return customers
        
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving all customers: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error retrieving customers: {e}")
        return []