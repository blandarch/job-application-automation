"""Imports WebElement and use_determiner"""

from selenium.webdriver.remote.webelement import WebElement
from ..interfaces.switcher import (
    use_determiner,
)


class MockJobWebsiteActions:
    """_summary_: Actions to interact with Mock Job Website automation"""

    def __init__(self, driver: WebElement):
        self.properties = use_determiner("Mock Website", driver)

    def go_to_login_page(self):
        """_summary_: method to go to the login page"""
        self.properties.driver.get(self.properties.login_url())

    def login(self, username: str, password: str):
        """_summary_: method to use to login to LinkedIn."""

        # sends username and password to the interface
        self.properties.username_element.send_keys(username)
        self.properties.password_element.send_keys(password)
        # clicks login
        self.properties.login_button_element.click()
