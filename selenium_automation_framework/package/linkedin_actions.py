"""Imports WebElement and use_determiner"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..interfaces.switcher import use_determiner
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
        # implicitly waits for 3 seconds
        self.properties.driver.implicitly_wait(3)

        # inputs job search text and presses enter
        self.properties.search_text_element.send_keys(search_text)
        self.properties.search_text_element.send_keys(Keys.ENTER)

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

            job_title_element = WebDriverWait(self.properties.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, self.properties.result_job_title_xpath)
                )
            )
            job_description_elements = WebDriverWait(self.properties.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, self.properties.result_job_description_xpath)
                )
            )
            company_element = WebDriverWait(self.properties.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, self.properties.result_job_company_xpath)
                )
            )
            job_url_element = WebDriverWait(self.properties.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.properties.url_xpath))
            )

            job_search_result = JobSearchResult(
                job_title=job_title_element.text,
                job_description=self.concatenate_job_description(
                    job_description_elements
                ),
                company=company_element.text,
                date_posted=None,
                url=job_url_element.get_attribute("href"),
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
            if element.tag_name == "p":
                p_text = element.find_element(By.XPATH, "./text()")
                job_description_text += p_text.text + "\n\n"
            # if tag is /ul, if will loop inside the /li elements to add the bullets inside the ul tag
            elif element.tag_name == "ul":
                # try:
                bullet_texts = []
                ul_children = element.find_elements(By.XPATH, "./span/li/text()")
                # except StaleElementReferenceException:
                #     ul_children = element.find_elements(By.XPATH, ".//li")
                # ul_children = element.find_elements(By.XPATH, "./li")
                # ul_children = WebDriverWait(self.properties.driver, 10).until(
                #     EC.visibility_of_all_elements_located((By.XPATH, ".//li"))
                #     # EC.visibility_of_all_elements_located()
                # )
                # bullet_texts = [li.text for li in ul_children if li.text]
                for li in ul_children:
                    # li.find_element(
                    #     By.XPATH,
                    #     '//*[@id="job-details"]/span/span[11]/ul/span[1]/li/text()',
                    # )
                    # li = self.properties.driver.find_element(
                    #     By.XPATH,
                    #     '//ul/span/li/text()',
                    # )
                    bullet_texts.append(li.text)
                job_description_text += "\n".join(bullet_texts)

        return job_description_text
