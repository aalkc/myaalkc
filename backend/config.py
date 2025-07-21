"""
Company configuration module for Amanat Al-Kalima Company.

This module contains all company details that are used throughout the application,
especially for generating invoices and reports.
"""

from typing import Dict, Any


class CompanyConfig:
    """
    Company configuration class containing all business details for Amanat Al-Kalima Company.
    
    This class stores essential company information including contact details,
    tax information, and business registration data.
    """
    
    # Company Basic Information
    COMPANY_NAME_ARABIC = "شركة أمانة الكلمة"
    COMPANY_NAME_ENGLISH = "Amanat Al-Kalima Company"
    OWNER_NAME = "Shahidul Islam"
    
    # Contact Information
    WEBSITE = "aalkco.com"
    CONTACT_NUMBER = "+966565790073"
    GENERAL_EMAIL = "contact@aalkco.com"
    
    # Address Information
    TAXPAYER_ADDRESS_ARABIC = "الدمام حي الخليج 23, 32425"
    TAXPAYER_ADDRESS_ENGLISH = "Dammam, Al Khaleej District 23, 32425"
    
    # Tax and Registration Information
    VAT_REGISTRATION_NUMBER = "313054315200003"
    TAX_PERIOD = "Quarterly"
    
    @classmethod
    def get_company_info(cls) -> Dict[str, Any]:
        """
        Get all company information as a dictionary.
        
        Returns:
            Dict[str, Any]: Complete company information dictionary
        """
        return {
            'company_name_arabic': cls.COMPANY_NAME_ARABIC,
            'company_name_english': cls.COMPANY_NAME_ENGLISH,
            'owner_name': cls.OWNER_NAME,
            'website': cls.WEBSITE,
            'contact_number': cls.CONTACT_NUMBER,
            'general_email': cls.GENERAL_EMAIL,
            'taxpayer_address_arabic': cls.TAXPAYER_ADDRESS_ARABIC,
            'taxpayer_address_english': cls.TAXPAYER_ADDRESS_ENGLISH,
            'vat_registration_number': cls.VAT_REGISTRATION_NUMBER,
            'tax_period': cls.TAX_PERIOD,
        }
    
    @classmethod
    def get_contact_info(cls) -> Dict[str, str]:
        """
        Get contact information only.
        
        Returns:
            Dict[str, str]: Contact information dictionary
        """
        return {
            'website': cls.WEBSITE,
            'contact_number': cls.CONTACT_NUMBER,
            'general_email': cls.GENERAL_EMAIL,
        }
    
    @classmethod
    def get_tax_info(cls) -> Dict[str, str]:
        """
        Get tax and registration information.
        
        Returns:
            Dict[str, str]: Tax information dictionary
        """
        return {
            'vat_registration_number': cls.VAT_REGISTRATION_NUMBER,
            'tax_period': cls.TAX_PERIOD,
            'taxpayer_address_arabic': cls.TAXPAYER_ADDRESS_ARABIC,
            'taxpayer_address_english': cls.TAXPAYER_ADDRESS_ENGLISH,
        }
    
    @classmethod
    def get_company_names(cls) -> Dict[str, str]:
        """
        Get company names in both languages.
        
        Returns:
            Dict[str, str]: Company names dictionary
        """
        return {
            'arabic': cls.COMPANY_NAME_ARABIC,
            'english': cls.COMPANY_NAME_ENGLISH,
        }


# Create a global instance for easy access
company_config = CompanyConfig()

# Also provide the information as a dictionary for backwards compatibility
COMPANY_INFO = CompanyConfig.get_company_info()