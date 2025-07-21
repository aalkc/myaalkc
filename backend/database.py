"""
Database connection module for MySQL 8.0 on Google Cloud SQL.

This module provides SQLAlchemy engine and session management for connecting
to a MySQL database instance hosted on Google Cloud SQL.
"""

import os
import logging
from typing import Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Base class for SQLAlchemy models
Base = declarative_base()

class DatabaseManager:
    """
    Database manager class for handling MySQL connections using SQLAlchemy.
    """
    
    def __init__(self):
        self.engine: Optional[Engine] = None
        self.SessionLocal: Optional[sessionmaker] = None
        
    def get_database_url(self) -> str:
        """
        Construct database URL from environment variables.
        
        Returns:
            str: Database URL for SQLAlchemy
            
        Raises:
            ValueError: If required environment variables are missing
        """
        # Database configuration from environment variables
        db_user = os.getenv('DB_USER', 'your_username')
        db_password = os.getenv('DB_PASSWORD', 'your_password')
        db_host = os.getenv('DB_HOST', 'your_cloud_sql_host')
        db_port = os.getenv('DB_PORT', '3306')
        db_name = os.getenv('DB_NAME', 'your_database_name')
        
        # Construct the database URL for mysql-connector-python
        database_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        
        logger.info(f"Connecting to database at {db_host}:{db_port}/{db_name}")
        return database_url
    
    def create_engine(self) -> Engine:
        """
        Create SQLAlchemy engine with connection pooling.
        
        Returns:
            Engine: SQLAlchemy engine instance
        """
        database_url = self.get_database_url()
        
        # Engine configuration for Google Cloud SQL
        engine = create_engine(
            database_url,
            poolclass=QueuePool,
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True,  # Validate connections before use
            pool_recycle=3600,   # Recycle connections after 1 hour
            echo=False,          # Set to True for SQL query logging
            connect_args={
                'charset': 'utf8mb4',
                'use_unicode': True,
                'autocommit': False,
            }
        )
        
        return engine
    
    def initialize_database(self) -> None:
        """
        Initialize database connection and create session factory.
        """
        try:
            self.engine = self.create_engine()
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            logger.info("Database connection initialized successfully")
        except SQLAlchemyError as e:
            logger.error(f"Failed to initialize database connection: {e}")
            raise
    
    def get_session(self) -> Session:
        """
        Get a database session.
        
        Returns:
            Session: SQLAlchemy session instance
            
        Raises:
            RuntimeError: If database is not initialized
        """
        if not self.SessionLocal:
            raise RuntimeError("Database not initialized. Call initialize_database() first.")
        
        return self.SessionLocal()
    
    def test_connection(self) -> bool:
        """
        Test database connection.
        
        Returns:
            bool: True if connection is successful, False otherwise
        """
        try:
            if not self.engine:
                self.initialize_database()
            
            with self.engine.connect() as connection:
                connection.execute("SELECT 1")
                logger.info("Database connection test successful")
                return True
        except SQLAlchemyError as e:
            logger.error(f"Database connection test failed: {e}")
            return False
    
    def close_connection(self) -> None:
        """
        Close database connection and dispose of engine.
        """
        if self.engine:
            self.engine.dispose()
            logger.info("Database connection closed")

# Global database manager instance
db_manager = DatabaseManager()

def get_db() -> Session:
    """
    Dependency function to get database session.
    
    Yields:
        Session: Database session
    """
    db = db_manager.get_session()
    try:
        yield db
    finally:
        db.close()

def init_db() -> None:
    """
    Initialize database connection.
    """
    db_manager.initialize_database()

def create_tables() -> None:
    """
    Create all tables defined in the Base metadata.
    """
    if not db_manager.engine:
        init_db()
    
    Base.metadata.create_all(bind=db_manager.engine)
    logger.info("Database tables created successfully")

# Example usage and testing
if __name__ == "__main__":
    # Initialize database
    init_db()
    
    # Test connection
    if db_manager.test_connection():
        print("✅ Database connection successful!")
    else:
        print("❌ Database connection failed!")
    
    # Clean up
    db_manager.close_connection()