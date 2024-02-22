"""_summary_: Login Properties interface class"""

from abc import ABC, abstractmethod


class LoginPropertiesInterface(ABC):
    """_summary_: Interface class for Login Properties"""

    @property
    @abstractmethod
    def _username(self):
        """_summary_: get method property for username"""

    @_username.setter
    @abstractmethod
    def _username(self, username: str):
        """_summary_: setter method property for username

        Args:
            username (str): username to be entered upon logging in
        """

    @property
    @abstractmethod
    def _password(self):
        """_summary_: get method property for password"""

    @_password.setter
    @abstractmethod
    def _password(self, password: str):
        """_summary_: setter method property for password

        Args:
            password (str): password to be entered upon logging in
        """

    @property
    @abstractmethod
    def login_successful_indicator(self):
        """_summary_: get method property for login_successful_indicator"""

    @login_successful_indicator.setter
    @abstractmethod
    def login_successful_indicator(self, value: str):
        """_summary_: setter method property for login_successful_indicator

        Args:
            value (str): indicator in the login page that the user was able to
                get into the website
        """

    def get_login_credentials(self):
        """_summary_: gets username and password from the website the user will be
            accessing with

        Returns:
            tuple(str, str): tuple of username and password
        """
        return self._username, self._password
