"""Python file that handles all overarching tests for the entire framework"""

from ..selenium_automation_framework.test.test_linkedin_actions import (
    test_linkedin_login,
    test_linkedin_login_wrong_password,
    test_linkedin_login_wrong_username,
)
from ..excel_framework.test.test_excel_framework import (
    test_add_data_to_empty_row_cell,
    test_add_data_with_existing_filename,
    test_add_data_without_filename,
)


def test_excel_framework():
    """_summary_: method that handles all tests for excel framework"""
    test_add_data_without_filename()
    test_add_data_to_empty_row_cell()
    test_add_data_with_existing_filename()


def test_selenium_automation_framework():
    """_summary_: method that handles all tests for selenium automation framework"""
    test_linkedin_login()
    test_linkedin_login_wrong_password()
    test_linkedin_login_wrong_username()
