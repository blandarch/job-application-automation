"""Imports Mock Job Website Actions and chromedriver"""

from ..webdriver_setup.driver_setup import chromedriver_setup
from ..package.mock_job_website_actions import MockJobWebsiteActions
from .test_helpers import TestHelpers


def test_mock_website_login():
    """_summary_: tests that framework is able to login using the mock website"""
    # sets up driver and mock website actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    mock_website_actions = TestHelpers.login_actions(mock_website_actions)

    # asserts that user is able to login
    assert (
        mock_website_actions.properties.driver.current_url
        != mock_website_actions.properties.login_url()
    )


def test_login_ui_get_set():
    """_summary_: tests that login_ui_interface is able to return different web elements"""
    # sets up driver and linkedIn actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    # assert is inside the login_ui_get_set() method
    TestHelpers.login_ui_get_set(
        instance=mock_website_actions,
        username_xpath='//*[text()="Username"]',
        password_xpath='//*[text()="Password"]',
        login_button_xpath='//*[text()="Forgot login info?"]',
    )
