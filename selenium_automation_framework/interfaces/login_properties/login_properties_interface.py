"""_summary_: Login Properties interface class"""

from cryptography.fernet import Fernet


class LoginPropertiesInterface:
    """_summary_: Interface class for Login Properties"""

    def __init__(self, username: str, password: str, login_successful_indicator: list):
        self._username: str = username
        self._password: str = password
        self._login_successful_indicator: list = login_successful_indicator

    @property
    def username(self):
        """_summary_: get method property for username"""
        return self._username

    @username.setter
    def username(self, username: str):
        """_summary_: setter method property for username

        Args:
            username (str): username to be entered upon logging in
        """
        self._username = username

    @property
    def password(self):
        """_summary_: get method property for password"""
        return self._password

    @password.setter
    def password(self, password: str):
        """_summary_: setter method property for password

        Args:
            password (str): password to be entered upon logging in
        """
        self._password = password

    @property
    def login_successful_indicator(self):
        """_summary_: get method property for login_successful_indicator"""
        return self._login_successful_indicator

    @login_successful_indicator.setter
    def login_successful_indicator(self, value: list):
        """_summary_: setter method property for login_successful_indicator

        Args:
            value (str): indicator in the login page that the user was able to
                get into the website
        """
        self._login_successful_indicator = value

    def get_login_credentials(self):
        """_summary_: gets username and password from the website the user will be
            accessing with

        Returns:
            tuple(str, str): tuple of username and password
        """
        return self.username, self.password

    def decrypt_credentials_value(self, key: str, encrypted_value: str):
        """_summary_: returns a decrypted value of an encrypted value, provided with a key.

        Args:
            key (str): a secret key that is used to provide access to decrypt encrypted value.
            encrypted_value (str): a value used for decrypting to its original text.

        Returns:
            str: a decrypted value of the original encrypted value.
        """

        # intialise fernet cypher with key
        cipher_suite = Fernet(key.encode())
        # decrypt the value back to it's original value
        decrypted_value = cipher_suite.decrypt(encrypted_value.encode())

        return decrypted_value.decode()
