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


def test_linkedin_login_wrong_username():
    """_summary_: method to test login with wrong username and right password"""

    # sets up driver and linkedIn actions instance
    driver = chromedriver_setup()
    linkedin_actions = LinkedInActions(driver)
    # sets up wrong username and right password
    wrong_username = "abc@gmail.com"
    password = linkedin_actions.properties.get_login_credentials()[1]

    # logs in
    linkedin_actions.go_to_login_page()
    linkedin_actions.login(wrong_username, password)

    # asserts that user is not able to login
    assert (
        linkedin_actions.properties.login_successful_indicator
        not in linkedin_actions.properties.driver.title
    )


def test_linkedin_login_wrong_password():
    """_summary_: method to test login with right username and wrong password"""

    # sets up driver and linkedIn actions instance
    driver = chromedriver_setup()
    linkedin_actions = LinkedInActions(driver)
    # sets up wrong username and right password
    wrong_username = linkedin_actions.properties.get_login_credentials()[0]
    password = "t3st1ngWronGP@assword"

    # logs in
    linkedin_actions.go_to_login_page()
    linkedin_actions.login(wrong_username, password)

    # asserts that user is not able to login
    assert (
        linkedin_actions.properties.login_successful_indicator
        not in linkedin_actions.properties.driver.title
    )
