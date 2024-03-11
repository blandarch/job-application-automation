"""Imports WebElement and use_determiner"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..interfaces.switcher import (
    use_determiner,
)
from ..objects.job_search_result import JobSearchResult


class MockJobWebsiteActions:
    """_summary_: Actions to interact with Mock Job Website automation"""

    def __init__(self, driver: WebElement):
        self.properties = use_determiner("Mock Website", driver)

    def go_to_main_website(self):
        """_summary_: method to go to the main mock website page"""
        self.properties.driver.get(self.properties.url)

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
        self.properties.search_button_element.click()

        self.properties.driver.implicitly_wait(5)

    def store_job_results(self) -> list[JobSearchResult]:
        """_summary_: returns a list of JobSearchResult object class to extract
            job details of search results

        Returns:
            list[JobSearchResult]: a list of Job Result object class that is filled
                up with job details per class
        """
        job_search_results: list[JobSearchResult] = []

        # loops through the job results and extracts the job title, description and company
        for result in self.properties.search_results_elements:
            job_search_results.append(
                JobSearchResult(
                    job_title=result.find_element(
                        By.XPATH, self.properties.result_job_title_xpath
                    ).text,
                    job_description=result.find_element(
                        By.XPATH, self.properties.result_job_description_xpath
                    ).text,
                    company=result.find_element(
                        By.XPATH, self.properties.result_job_company_xpath
                    ).text,
                    date_posted=None,
                )
            )

        return job_search_results
