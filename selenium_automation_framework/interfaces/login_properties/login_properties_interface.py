"""_summary_: Login Properties interface class"""

from abc import ABC, abstractmethod
from cryptography.fernet import Fernet


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

    def decrypt_credentials_value(self, key: str, encrypted_value: str):
        """_summary_: returns a decrypted value of an encrypted value, provided with a key.

        Args:
            key (str): a secret key that is used to provide access to decrypt encrypted value.
            encrypted_value (str): a value used for decrypting to its original text.

        Returns:
            str: a decrypted value of the original encrypted value.
        """

        # intialise fernet cypher with key
        cipher_suite = Fernet(key)
        # decrypt the value back to it's original value
        decrypted_value = cipher_suite.decrypt(encrypted_value)

        return decrypted_value.decode()
