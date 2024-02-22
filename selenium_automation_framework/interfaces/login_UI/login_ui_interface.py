"""Login UI Interface class"""

from abc import ABC, abstractmethod


class LoginUIInterface(ABC):
    """_summary_: Interface class for Login UI Interface"""

    @property
    @abstractmethod
    def _username_xpath(self):
        """_summary_: get method property for username xpath"""

    @_username_xpath.setter
    @abstractmethod
    def _username_xpath(self, xpath: str):
        """_summary_: setter method property for username xpath

        Args:
            xpath (str): xpath of determiner to be used in getting username element
        """

    @property
    @abstractmethod
    def _password_xpath(self):
        """_summary_: get method property for password xpath"""

    @_password_xpath.setter
    @abstractmethod
    def _password_xpath(self, xpath: str):
        """_summary_: setter method property for password xpath

        Args:
            xpath (str): xpath of determiner to be used in getting password element
        """

    @property
    @abstractmethod
    def _login_button_xpath(self):
        """_summary_: get method property for login button xpath"""

    @_login_button_xpath.setter
    @abstractmethod
    def _login_button_xpath(self):
        """_summary_: setter method property for login button xpath

        Args:
            xpath (str): xpath of determiner to be used in getting login button
        """

    ######################## WEBDRIVER ELEMENT PROPERTIES #############################
    @property
    @abstractmethod
    def username_element(self):
        """_summary_: get method property for username element"""

    @username_element.setter
    @abstractmethod
    def username_element(self, element):
        """_summary_: setter method property for username element

        Args:
            element (_type_): element where element of username is stored
                for caching.
        """

    @property
    @abstractmethod
    def password_element(self):
        """_summary_: get method property for password element"""

    @password_element.setter
    @abstractmethod
    def password_element(self, element):
        """_summary_: setter method property for password element

        Args:
            element (_type_): element where element of password is stored
                for caching.
        """

    @property
    @abstractmethod
    def login_button_element(self):
        """_summary_: get method property for login button element"""

    @login_button_element.setter
    def login_button_element(self):
        """_summary_: setter method property for login button element

        Args:
            element (_type_): element where element of login button is stored
                for caching.
        """
