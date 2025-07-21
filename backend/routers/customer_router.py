"""
Customer API router with FastAPI endpoints.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_db
from .. import customer_crud, schemas


router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(
    customer: schemas.CustomerCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new customer.
    
    Args:
        customer: Customer data to create
        db: Database session
        
    Returns:
        Created customer data
        
    Raises:
        HTTPException: If customer with email already exists
    """
    # Check if customer with email already exists
    existing_customer = customer_crud.get_customer_by_email(db, email=customer.email)
    if existing_customer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer with this email already exists"
        )
    
    try:
        return customer_crud.create_customer(db=db, customer=customer)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer with this email already exists"
        )


@router.get("/", response_model=List[schemas.CustomerResponse])
def get_customers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get a list of all customers with pagination.
    
    Args:
        skip: Number of records to skip (default: 0)
        limit: Maximum number of records to return (default: 100)
        db: Database session
        
    Returns:
        List of customer data
    """
    customers = customer_crud.get_customers(db, skip=skip, limit=limit)
    return customers


@router.get("/{customer_id}", response_model=schemas.CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a single customer by their ID.
    
    Args:
        customer_id: ID of the customer to retrieve
        db: Database session
        
    Returns:
        Customer data
        
    Raises:
        HTTPException: If customer is not found
    """
    customer = customer_crud.get_customer(db, customer_id=customer_id)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    return customer