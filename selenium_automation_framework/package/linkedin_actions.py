"""Imports WebElement and use_determiner"""

from selenium.webdriver.remote.webelement import WebElement
from ..interfaces.switcher import (
    use_determiner,
)


class LinkedInActions:
    """_summary_: Actions to interact with LinkedIn automation"""

    def __init__(self, driver: WebElement):
        self.properties = use_determiner("LinkedIn", driver)

    def go_to_login_page(self):
        """_summary_: method to go to the login page"""
        self.properties.driver.get(self.properties.login_url())

    def login(self):
        """_summary_: method to use to login to LinkedIn."""

        credentials = self.properties.get_login_credentials()

        # sends username and password to the interface
        self.properties.username_element.send_keys(credentials[0])
        self.properties.password_element.send_keys(credentials[1])
        # clicks login
        self.properties.login_button_element.click()
