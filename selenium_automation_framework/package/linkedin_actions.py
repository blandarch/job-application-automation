"""Imports WebElement and use_determiner"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from ..interfaces.switcher import (
    use_determiner,
)
from ..objects.job_search_result import JobSearchResult


class LinkedInActions:
    """_summary_: Actions to interact with LinkedIn automation"""

    def __init__(self, driver: WebElement):
        self.properties = use_determiner("LinkedIn", driver)

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
        """_summary_: method to use to search for jobs in linkedin.

        Args:
            search_text (str): the text you will input for the job search text
        """
        # clicks the Jobs Web Element after logging in
        self.properties.jobs_button_element.click()

        # inputs job search text and presses enter
        self.properties.search_text_element.send_keys(search_text)
        self.properties.search_button_element.send_keys(Keys.ENTER)

        # implicitly waits for 5 seconds
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
            result.click()

            job_search_result = JobSearchResult(
                job_title=self.properties.get_web_element(
                    self.properties.result_job_title_xpath, self.properties.driver
                ).text,
                # need logic on how to split html elements within the job description element
                job_description=self.concatenate_job_description(
                    self.properties.get_web_elements(
                        self.properties.result_job_description_xpath,
                        self.properties.driver,
                    )
                ),
                company=self.properties.get_web_element(
                    self.properties.result_job_company_xpath, self.properties.driver
                ).text,
                date_posted=None,
                url=self.properties.get_web_element(
                    self.properties.url_xpath, self.properties.driver
                ).get_attribute("href"),
            )
            job_search_results.append(job_search_result)

        return job_search_results

    def concatenate_job_description(
        self, job_description_elements: list[WebElement]
    ) -> str:
        """_summary_: action method to use to concatenate Job Description texts from
            LinkedIn from the children elements

        Args:
            job_description_elements (list[WebElement]): the overall job description parent
                element which will be the basis for the project to loop over

        Returns:
            str: the combined text from job description from different elements
        """
        # initialises empty string to be concatenated
        job_description_text = ""

        # loops through the the job description elements to add text to job_description_text
        for element in job_description_elements:
            # if tag name is "/p" then it will just concatenate the text that is available
            if element.tag_name == "p" and (
                element.text is not None and element.text != ""
            ):
                job_description_text += element.text + "\n\n"
            # if tag is /ul, if will loop inside the /li elements to add the bullets inside the ul tag
            elif element.tag_name == "ul" and (
                element.text is not None and element.text != ""
            ):
                ul_children = element.find_elements(By.XPATH, "./li")
                bullet_texts = [li.text for li in ul_children]
                job_description_text += "\n".join(bullet_texts)

        return job_description_text
