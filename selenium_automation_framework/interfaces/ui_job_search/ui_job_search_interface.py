"""Job Search UI Interface Class"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class UIJobSearchInterface:
    """_summary_: Interface class for Job Search"""

    def __init__(self, driver: webdriver.Chrome, search_text_xpath: str):
        self.driver: webdriver.Chrome = driver
        self._search_text_xpath: str = search_text_xpath
        # Element variables
        self._search_text_element: WebElement = None

    @property
    def search_text_element(self) -> WebElement:
        """_summary_: setter method property for search text element

        Returns:
            WebElement: web element for the search text
        """
        if self._search_text_element is None:
            return self.driver.find_element(By.XPATH, self._search_text_xpath)
        return self._search_text_element

    @search_text_element.setter
    def search_text_element(self, xpath: str):
        """_summary_: setter method property for search text element

        Args:
            xpath (str): updated xpath element for search text
        """
        self._search_text_xpath = xpath
        self._search_text_element = self.driver.find_element(
            By.XPATH, self._search_text_xpath
        )
