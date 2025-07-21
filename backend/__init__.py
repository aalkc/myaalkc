"""
Backend package for myaalkc application.
"""

from .database import db_manager, get_db, init_db, create_tables, Base
from .config import CompanyConfig, company_config, COMPANY_INFO

__all__ = [
    'db_manager',
    'get_db', 
    'init_db',
    'create_tables',
    'Base',
    'CompanyConfig',
    'company_config',
    'COMPANY_INFO'
]