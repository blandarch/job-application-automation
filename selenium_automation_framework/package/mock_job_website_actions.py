"""Imports WebElement and use_determiner"""

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from ..interfaces.switcher import (
    use_determiner,
)
from ..objects.job_search_result import JobSearchResult


class MockJobWebsiteActions:
    """_summary_: Actions to interact with Mock Job Website automation"""

    def __init__(self, driver: WebElement):
        self.properties = use_determiner("Mock Website", driver)

    def go_to_login_page(self):
        """_summary_: method to go to the login page"""
        self.properties.driver.get(self.properties.login_url())

    def login(self, username: str, password: str):
        """_summary_: method to use to login to LinkedIn."""

        # sends username and password to the interface
        self.properties.username_element.send_keys(username)
        self.properties.password_element.send_keys(password)
        # clicks login
        self.properties.login_button_element.click()

    def search_jobs(self, search_text: str):
        """_summary_: method to use when searching for jobs in the mock website

        Args:
            search_text (str): text to be inputed in the job search
        """
        # goes to the job search website for the mock website
        self.properties.driver.get(self.properties.url)

        # inputs job search and presses enter
        self.properties.search_text_element.send_keys(search_text)
        self.properties.search_text_element.send_keys(Keys.ENTER)

    def store_job_results(self):
        # update search text xpath
        self.properties.search_text_element = '//input[@id="criterion271_35"]'
        
        
