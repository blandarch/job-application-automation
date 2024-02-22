"""Imports LinkedIn Actions and chromedriver"""

from ..webdriver_setup.driver_setup import (
    chromedriver_setup,
)
from ..package.linkedin_actions import LinkedInActions


def test_linkedin_login():
    """_summary_: tests that framework is able to login using LinkedIn"""
    # sets up driver and linkedIn actions instance
    driver = chromedriver_setup()
    linkedin_actions = LinkedInActions(driver)
    username, password = linkedin_actions.properties.get_login_credentials()

    # logs in
    linkedin_actions.go_to_login_page()
    linkedin_actions.login(username, password)

    # asserts that user is able to login
    assert (
        linkedin_actions.properties.login_successful_indicator
        in linkedin_actions.properties.driver.title
    )
