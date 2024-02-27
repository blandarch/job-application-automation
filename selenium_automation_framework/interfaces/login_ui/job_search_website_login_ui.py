"""Imports Webdriver and LoginUIInterface class"""

from selenium import webdriver
from .login_ui_interface import LoginUIInterface


class JobSearchWebsiteLoginUI(LoginUIInterface):
    """_summary_: Inherits login_ui_interface to provide xpath and
    elements to mock website Login UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver=driver,
            username_xpath='//input[@id="email"]',
            password_xpath='//input[@id="password"]',
            login_buton_xpath='//input[@type="button"][@name="submit.login"]',
        )
