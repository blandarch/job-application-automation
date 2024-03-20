"""Job Search UI Interface Class"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class UIJobResultsInterface:
    """_summary_: Interface class for Job Search"""

    def __init__(
        self,
        driver: webdriver.Chrome,
        results_search_text_xpath: str,  # search text bar xpath in job results page
        search_results_xpath: str,  # generic xpath for all job results appeared
        result_job_title_xpath: str,
        result_job_description_xpath: str,
        result_job_company_xpath: str,
    ):
        self.driver: webdriver.Chrome = driver
        self._results_search_text_xpath: str = results_search_text_xpath
        self._search_results_xpath: str = search_results_xpath
        self._result_job_title_xpath: str = result_job_title_xpath
        self._result_job_description_xpath: str = result_job_description_xpath
        self._result_job_company_xpath: str = result_job_company_xpath

        # Element variables
        self._results_search_text_element: WebElement = (
            None  # search text bar element in job results page
        )
        self._search_results_elements: list[WebElement] = (
            None  # list of elements for all job results appeared
        )

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

    ######GENERIC JOB RESULTS ELEMENT##########

    @property
    def search_results_elements(self) -> list[WebElement]:
        """_summary_: property to set generic job result web elements

        Returns:
            list[WebElement]: a list of web elements for all job results
        """
        if self._search_results_elements is None:
            return self.driver.find_elements(By.XPATH, self._search_results_xpath)
        return self._search_results_elements

    @search_results_elements.setter
    def search_results_elements(self, xpath: str):
        self._search_results_xpath = xpath
        self._search_results_elements = self.driver.find_elements(
            By.XPATH, self._search_results_xpath
        )

    #####JOB RESULTS ELEMENTS PROPERTIES#########
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

    @staticmethod
    def get_element_xpath(xpath: str, driver: webdriver.Chrome) -> WebElement:
        """_summary_: method to use to get element xpath with the concatonated xpaths
            from job results

        Args:
            xpath (str): xpath as basis to find web element
            driver (webdriver.Chrome): driver that orchestrates the automation

        Returns:
            WebElement: Web Element retrieved
        """
        return driver.find_element(By.XPATH, xpath)

    @staticmethod
    def get_web_elements(xpath: str, driver: webdriver.Chrome) -> list[WebElement]:
        """_summary_: method to use to get elements with the concatonated xpaths
            from job results

        Args:
            xpath (str): xpath as basis to find web element
            driver (webdriver.Chrome): driver that orchestrates the automation

        Returns:
            WebElement: list of Web Elements retrieved
        """
        return driver.find_elements(By.XPATH, xpath)
