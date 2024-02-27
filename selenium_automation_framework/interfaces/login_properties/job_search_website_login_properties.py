"""Imports LoginPropertiesInterface class"""

import json

from .login_properties_interface import (
    LoginPropertiesInterface,
)
from .static_constants import KEY, PASSWORD, USERNAME
from .login_properties_paths_constants import JOB_SEARCH_WEBSITE_CREDENTIALS_JSON


class JobSearchWebsiteLoginProperties(LoginPropertiesInterface):
    """_summary_: Inherits login_properties_interface to provide username
    and password to mock job website Login"""

    def __init__(self):
        with open(JOB_SEARCH_WEBSITE_CREDENTIALS_JSON, encoding="utf-8") as file:
            self.data = json.load(file)

        # passes and decrypts the username password with a key provided in json
        super().__init__(
            self.decrypt_credentials_value(self.data[KEY], self.data[USERNAME]),
            self.decrypt_credentials_value(self.data[KEY], self.data[PASSWORD]),
        )
