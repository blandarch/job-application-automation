"""Login UI Interface class"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginUIInterface:
    """_summary_: Interface class for Login UI Interface"""

    def __init__(
        self,
        driver: webdriver.Chrome,
        username_xpath: str,
        password_xpath: str,
        login_buton_xpath: str,
    ):
        self.driver = driver
        self._username_xpath: str = username_xpath
        self._password_xpath: str = password_xpath
        self._login_button_xpath: str = login_buton_xpath
        # Element Variables
        self._username_element: WebElement = None
        self._password_element: WebElement = None
        self._login_button_element: WebElement = None

    @property
    def username_xpath(self):
        """_summary_: get method property for username xpath"""
        return self._username_xpath

    @username_xpath.setter
    def username_xpath(self, xpath: str):
        """_summary_: setter method property for username xpath

        Args:
            xpath (str): xpath of determiner to be used in getting username element
        """
        self._username_xpath = xpath

    @property
    def password_xpath(self):
        """_summary_: get method property for password xpath"""
        return self._password_xpath

    @password_xpath.setter
    def password_xpath(self, xpath: str):
        """_summary_: setter method property for password xpath

        Args:
            xpath (str): xpath of determiner to be used in getting password element
        """
        self._password_xpath = xpath

    @property
    def login_button_xpath(self):
        """_summary_: get method property for login button xpath"""
        return self._login_button_xpath

    @login_button_xpath.setter
    def login_button_xpath(self, xpath: str):
        """_summary_: setter method property for login button xpath

        Args:
            xpath (str): xpath of determiner to be used in getting login button
        """
        self._login_button_xpath = xpath

    ######################## WEBDRIVER ELEMENT PROPERTIES #############################
    @property
    def username_element(self):
        """_summary_: get method property for username element"""
        if self._username_element is None:
            return self.driver.find_element(By.XPATH, self._username_xpath)
        return self._username_element

    @username_element.setter
    def username_element(self, element: WebElement):
        """_summary_: setter method property for username element

        Args:
            element (_type_): element where element of username is stored
                for caching.
        """
        self._username_element = element

    @property
    def password_element(self):
        """_summary_: get method property for password element"""
        if self._password_element is None:
            return self.driver.find_element(By.XPATH, self._password_xpath)
        return self._password_element

    @password_element.setter
    def password_element(self, element: WebElement):
        """_summary_: setter method property for password element

        Args:
            element (_type_): element where element of password is stored
                for caching.
        """
        self._password_element = element

    @property
    def login_button_element(self):
        """_summary_: get method property for login button element"""
        if self._login_button_element is None:
            return self.driver.find_element(By.XPATH, self._login_button_xpath)
        return self._login_button_element

    @login_button_element.setter
    def login_button_element(self, element: WebElement):
        """_summary_: setter method property for login button element

        Args:
            element (_type_): element where element of login button is stored
                for caching.
        """
        self._login_button_element = element
