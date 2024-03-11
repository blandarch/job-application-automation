"""Imports Webdriver and Interface"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .ui_job_search_interface import UIJobSearchInterface


class UIMockWebsiteJobSearch(UIJobSearchInterface):
    """Inherited class for Mock Website Job Search UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver,
            search_text_xpath='//input[contains(@id, "criterion271")]',
            search_button_xpath='//input[@type="button"][@value="Search Jobs"]',
        )
        self._search_button_xpath: str = (
            '//input[@type="button"][@value="Search Jobs"]',
        )
        # Element Variables
        self._search_button_element: WebElement = None

    @property
    def search_button_element(self) -> WebElement:
        """_summary_: setter method property for search button element

        Returns:
            WebElement: web element for the search text
        """
        if self._search_button_element is None:
            return self.driver.find_element(By.XPATH, self._search_button_xpath)
        return self._search_button_element

    @search_button_element.setter
    def search_button_element(self, xpath: str):
        self._search_button_xpath = xpath
        self._search_button_element = self.driver.find_element(
            By.XPATH, self._search_button_xpath
        )
