"""Imports LinkedIn Actions and chromedriver"""

from ..webdriver_setup.driver_setup import chromedriver_setup
from ..package.linkedin_actions import LinkedInActions
from .test_helpers import TestHelpers


def test_linkedin_login():
    """_summary_: tests that framework is able to login using LinkedIn"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    linkedin_actions = TestHelpers.login_actions(linkedin_actions)

    # asserts that user is able to login
    assert (
        linkedin_actions.properties.driver.current_url
        != linkedin_actions.properties.login_url()
    )


def test_ui_get_set():
    """_summary_: tests that login_ui_interface is able to return different web elements"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    # assert is inside the login_ui_get_set() method
    TestHelpers.login_ui_get_set(
        instance=linkedin_actions,
        username_xpath='//label[contains(text(), "Email")]',
        password_xpath='//label[contains(text(), "Password")]',
        login_button_xpath='//*[contains(text(), "Forgot password?")]',
    )
