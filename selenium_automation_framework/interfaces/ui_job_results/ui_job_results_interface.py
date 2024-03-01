"""Job Search UI Interface Class"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class UIJobResultsInterface:
    """_summary_: Interface class for Job Search"""

    def __init__(
        self,
        driver: webdriver.Chrome,
        results_search_text_xpath: str,
        result_job_title_xpath: str,
        result_job_description_xpath: str,
        result_job_company_xpath: str,
        result_date_opened_xpath: str,
    ):
        self.driver: webdriver.Chrome = driver
        self._results_search_text_xpath: str = results_search_text_xpath
        self._result_job_title_xpath: str = result_job_title_xpath
        self._result_job_description_xpath: str = result_job_description_xpath
        self._result_job_company_xpath: str = result_job_company_xpath
        self._result_date_opened_xpath: str = result_date_opened_xpath

        # Element variables
        self._results_search_text_element: WebElement = None

    @property
    def results_search_text_element(self) -> WebElement:
        """_summary_: setter method property for search text element

        Returns:
            WebElement: web element for the search text
        """
        if self._results_search_text_element is None:
            return self.driver.find_element(By.XPATH, self._results_search_text_xpath)
        return self._results_search_text_element

    @results_search_text_element.setter
    def results_search_text_element(self, xpath: str):
        """_summary_: setter method property for search text element

        Args:
            xpath (str): updated xpath element for search text
        """
        self._results_search_text_xpath = xpath
        self._results_search_text_element = self.driver.find_element(
            By.XPATH, self._results_search_text_xpath
        )

    @property
    def result_job_title_xpath(self) -> str:
        """_summary_: xpath property for job title xpath

        Returns:
            str: xpath for job title
        """
        return self._result_job_title_xpath

    @result_job_title_xpath.setter
    def result_job_title_xpath(self, xpath: str):
        self._result_job_title_xpath = xpath

    @property
    def result_job_description_xpath(self) -> str:
        """_summary_: xpath property for job description xpath

        Returns:
            str: xpath for job description
        """
        return self._result_job_description_xpath

    @result_job_description_xpath.setter
    def result_job_description_xpath(self, xpath: str):
        self._result_job_description_xpath = xpath

    @property
    def result_job_company_xpath(self) -> str:
        """_summary_: xpath property for job company xpath

        Returns:
            str: xpath for job company
        """
        return self._result_job_company_xpath

    @result_job_company_xpath.setter
    def result_job_company_xpath(self, xpath: str):
        self._result_job_company_xpath = xpath

    @property
    def result_date_opened_xpath(self) -> str:
        """_summary_: xpath property for date opened xpath

        Returns:
            str: xpath for date opened
        """
        return self._result_date_opened_xpath

    @result_date_opened_xpath.setter
    def result_date_opened_xpath(self, xpath: str):
        self._result_date_opened_xpath = xpath
