"""imports Selenium and UIJobResultsInterface"""

from selenium import webdriver

from .ui_job_results_interface import UIJobResultsInterface


class UIJobResultsLinkedIn(UIJobResultsInterface):
    """_summary_: UI Properties for LinkedIn Job Results

    Args:
        UIJobResultsInterface (_type_): the common job interface
    """

    def __init__(
        self,
        driver: webdriver.Chrome,
    ):
        super().__init__(
            driver,
            results_search_text_xpath='//input[contains(@id, "jobs-search-box-keyword-id")]',
            search_results_xpath='//li[contains(@id, "ember")][not(contains(@class, "artdeco"))]',
            result_job_title_xpath='//h2[contains(@class, "job-title")]/a/span',
            result_job_description_xpath='//div[@id="job-details"]//span/p | //span/ul',
            result_job_company_xpath='//a[@class="app-aware-link "][contains(@href, "/company/")]',
        )
        self._url_xpath = '//h2[contains(@class, "job-title")]/a'

    @property
    def url_xpath(self) -> str:
        """_summary_: get set method to retrieve the url xpath property for LinkedIn

        Returns:
            str: the xpath that will be used as web element
        """
        return self._url_xpath

    @url_xpath.setter
    def url_xpath(self, xpath: str):
        self._url_xpath = xpath
