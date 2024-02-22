"""Imports Webdriver and LoginUIInterface class"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_automation_framework.interfaces.login_UI.login_ui_interface import (
    LoginUIInterface,
)


class LinkedInLoginUI(LoginUIInterface):
    """_summary_: Inherits login_ui_interface to provide xpath and elements to LinkedIn Login UI"""

    def __init__(self, driver: webdriver.Chrome):
        self.driver: webdriver.Chrome = driver
        self._username_xpath: str = "Username"  # temporary value
        self._password_xpath: str = "Password"  # temporary value
        self._login_button_xpath: str = "Login"  # temporary value
        # element variables
        self.username_element: WebElement = None
        self.password_element: WebElement = None
        self.login_button_element: WebElement = None

    ################# XPATHS PROPERTIES #####################

    @property
    def _username_xpath(self):
        return self._username_xpath

    @_username_xpath.setter
    def _username_xpath(self, xpath: str):
        self._username_xpath = xpath

    @property
    def _password_xpath(self):
        return self._password_xpath

    @_password_xpath.setter
    def _password_xpath(self, xpath: str):
        self._password_xpath = xpath

    @property
    def _login_button_xpath(self):
        return self._login_button_xpath

    @_login_button_xpath.setter
    def _login_button_xpath(self, xpath: str):
        self._login_button_xpath = xpath

    ################# ELEMENT PROPERTIES #####################

    @property
    def username_element(self):
        if self.username_element is None:
            return self.driver.find_element(By.XPATH, self._username_xpath)
        return self.username_element

    @username_element.setter
    def username_element(self, element: WebElement):
        self.username_element = element

    @property
    def password_element(self):
        if self.password_element is None:
            return self.driver.find_element(By.XPATH, self._password_xpath)
        return self.password_element

    @password_element.setter
    def password_element(self, element: WebElement):
        self.password_element = element

    @property
    def login_button_element(self):
        if self.login_button_element is None:
            return self.driver.find_element(By.XPATH, self._login_button_xpath)
        return self.login_button_element

    @login_button_element.setter
    def login_button_element(self, element: WebElement):
        self.login_button_element = element
