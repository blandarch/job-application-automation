"""Imports Webdriver and LoginUIInterface class"""

from selenium import webdriver
from .login_ui_interface import LoginUIInterface


class JobSearchWebsiteLoginUI(LoginUIInterface):
    """_summary_: Inherits login_ui_interface to provide xpath and
    elements to mock website Login UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver=driver,
            username_xpath='//input[@name="username"]',
            password_xpath='//input[@name="password"]',
            login_buton_xpath='//input[@type="submit"][@class="button"]',
        )
