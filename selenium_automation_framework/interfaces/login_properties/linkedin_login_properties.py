"""Imports LoginPropertiesInterface class"""

from selenium_automation_framework.interfaces.login_properties.login_properties_interface import (
    LoginPropertiesInterface,
)


class LinkedInLoginProperties(LoginPropertiesInterface):
    """_summary_: Inherits login_properties_interface to provide username
    and password to LinkedIn Login"""

    def __init__(self):
        self.username: str = None
        self.password: str = None

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username: str):
        self.username = username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password: str):
        self.password = password
