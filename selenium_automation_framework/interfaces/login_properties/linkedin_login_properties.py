"""Imports LoginPropertiesInterface class"""

import json

from selenium_automation_framework.interfaces.login_properties.login_properties_interface import (
    LoginPropertiesInterface,
)


class LinkedInLoginProperties(LoginPropertiesInterface):
    """_summary_: Inherits login_properties_interface to provide username
    and password to LinkedIn Login"""

    def __init__(self):
        with open("./../../credentials/linkedin.json", encoding="utf-8") as file:
            self.data = json.load(file)

        # passes and decrypts the username password with a key provided in json
        self._username: str = self.decrypt_credentials_value(
            self.data["key"], self.data["username"]
        )
        self._password: str = self.decrypt_credentials_value(
            self.data["key"], self.data["password"]
        )
        self.login_successful_indicator: str = "Feed"

    @property
    def _username(self):
        return self._username

    @_username.setter
    def _username(self, username: str):
        self._username = username

    @property
    def _password(self):
        return self._password

    @_password.setter
    def _password(self, password: str):
        self._password = password

    @property
    def login_successful_indicator(self):
        return self.login_successful_indicator

    @login_successful_indicator.setter
    def login_successful_indicator(self, value: str):
        self.login_successful_indicator = value
