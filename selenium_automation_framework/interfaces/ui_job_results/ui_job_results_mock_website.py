"""Job Search UI Inheritance Class for Mock Website"""

from selenium import webdriver

from .ui_job_results_interface import UIJobResultsInterface


class UIJobResultsMockWebsite(UIJobResultsInterface):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver,
            results_search_text_xpath='//input[@id="criterion271_27"]',
            search_results_xpath='//div[contains(@class, "s-res")]',
            result_job_title_xpath="//h3/a",
            result_job_description_xpath="Job Description",
            result_job_company_xpath="""//p[@class="search-result-item-company-name"]
                /span[class="companyName"]""",
        )
