"""Imports Webdriver and Interface"""

from selenium import webdriver
from .ui_job_search_interface import UIJobSearchInterface


class UIMockWebsiteJobSearch(UIJobSearchInterface):
    """Inherited class for Mock Website Job Search UI"""

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(
            driver, search_text_xpath='//input[contains(@id, "criterion271")]'
        )
