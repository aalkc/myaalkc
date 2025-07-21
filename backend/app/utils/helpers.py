"""
Utility helper functions
"""

import string
import random
from datetime import datetime


def generate_order_number(prefix: str = "ORD") -> str:
    """Generate a unique order number"""
    timestamp = datetime.now().strftime("%Y%m%d")
    random_suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}-{timestamp}-{random_suffix}"


def format_currency(amount: float, currency: str = "SAR") -> str:
    """Format currency amount"""
    return f"{amount:,.2f} {currency}"


def calculate_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Calculate tax amount (Saudi VAT is 15%)"""
    return amount * tax_rate


def calculate_total_with_tax(amount: float, tax_rate: float = 0.15) -> float:
    """Calculate total amount including tax"""
    return amount + calculate_tax(amount, tax_rate)