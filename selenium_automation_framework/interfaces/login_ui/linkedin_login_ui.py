"""Imports Webdriver and LoginUIInterface class"""

from selenium import webdriver
from .login_ui_interface import LoginUIInterface


class LinkedInLoginUI(LoginUIInterface):
    """_summary_: Inherits login_ui_interface to provide xpath and elements to LinkedIn Login UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver=driver,
            username_xpath='//input[@id="username"]',
            password_xpath='//input[@id="password"]',
            login_buton_xpath='//button[@type="submit"]',
        )
