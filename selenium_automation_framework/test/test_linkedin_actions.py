"""Imports LinkedIn Actions and chromedriver"""

from ..webdriver_setup.driver_setup import chromedriver_setup
from ..package.linkedin_actions import LinkedInActions


def test_linkedin_login():
    """_summary_: tests that framework is able to login using LinkedIn"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    username, password = linkedin_actions.properties.get_login_credentials()

    # logs in
    linkedin_actions.go_to_login_page()
    linkedin_actions.login(username, password)

    # asserts that user is able to login
    assert (
        linkedin_actions.properties.driver.current_url
        != linkedin_actions.properties.login_url()
    )


def test_ui_get_set():
    """_summary_: tests that login_ui_interface is able to return different web elements"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    linkedin_actions.go_to_login_page()

    # retrieves original elements for username, password and login
    original_username_element = linkedin_actions.properties.username_element
    original_password_element = linkedin_actions.properties.password_element
    original_login_element = linkedin_actions.properties.login_button_element

    # passes different xpath for username, password, and login elements
    linkedin_actions.properties.username_element = '//label[contains(text(), "Email")]'
    linkedin_actions.properties.password_element = (
        '//label[contains(text(), "Password")]'
    )
    linkedin_actions.properties.login_button_element = (
        '//*[contains(text(), "Forgot password?")]'
    )

    # asserts that the original elements are different from the new elements inserted by xpath
    assert original_username_element != linkedin_actions.properties.username_element
    assert original_password_element != linkedin_actions.properties.password_element
    assert original_login_element != linkedin_actions.properties.login_button_element
