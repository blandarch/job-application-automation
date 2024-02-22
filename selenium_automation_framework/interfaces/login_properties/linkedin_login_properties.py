"""Imports LoginPropertiesInterface class"""

import json

from .login_properties_interface import (
    LoginPropertiesInterface,
)
from .static_constants import KEY, PASSWORD, USERNAME
from .login_properties_paths_constants import (
    LINKEDIN_CREDENTIALS_JSON,
)


class LinkedInLoginProperties(LoginPropertiesInterface):
    """_summary_: Inherits login_properties_interface to provide username
    and password to LinkedIn Login"""

    def __init__(self):
        with open(LINKEDIN_CREDENTIALS_JSON, encoding="utf-8") as file:
            self.data = json.load(file)

        # passes and decrypts the username password with a key provided in json
        super().__init__(
            self.decrypt_credentials_value(self.data[KEY], self.data[USERNAME]),
            self.decrypt_credentials_value(self.data[KEY], self.data[PASSWORD]),
            ["Feed", "Security Verification | LinkedIn"],
        )
