"""Imports Webdriver and Interface"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .ui_job_search_interface import UIJobSearchInterface


class UILinkedInJobSearch(UIJobSearchInterface):
    """Inherited class for LinkedIn Job Search UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver, search_text_xpath='//input[contains(@class, "jobs-search-box")]'
        )
        self._jobs_button_xpath: str = '//a[contains(@href, "jobs")]/..'

        # Element variables
        self._jobs_button_element: WebElement = None

    @property
    def jobs_button_element(self) -> WebElement:
        """_summary_: setter method property for job button element

        Returns:
            WebElement: web element for the job button
        """
        if self._jobs_button_element is None:
            return self.driver.find_element(By.XPATH, self._jobs_button_xpath)
        return self._jobs_button_element

    @jobs_button_element.setter
    def jobs_button_element(self, xpath: str):
        self._jobs_button_xpath = xpath
        self._jobs_button_element = self.driver.find_element(
            By.XPATH, self._jobs_button_xpath
        )
