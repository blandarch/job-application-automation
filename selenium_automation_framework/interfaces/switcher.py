"""Inherits WebElement, and Inheritances from parents properties"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver

# from links folder
from .links.linkedin_login import LinkedInLogin
from .links.job_search_website_login import JobSearchWebsiteLinks

# from login properties folder
from .login_properties.linkedin_login_properties import (
    LinkedInLoginProperties,
)
from .login_properties.job_search_website_login_properties import (
    JobSearchWebsiteLoginProperties,
)

# from login_ui folder
from .ui_login.linkedin_login_ui import (
    LinkedInLoginUI,
)
from .ui_login.job_search_website_login_ui import JobSearchWebsiteLoginUI

# from ui_job_search folder
from .ui_job_search.ui_mock_website_job_search import UIMockWebsiteJobSearch


class LinkedInPropertiesSwitcher(
    LinkedInLogin, LinkedInLoginProperties, LinkedInLoginUI
):
    """_summary_: Inherits all properties from LinkedInLogin,
    LinkedInLoginProperties, LinkedInLoginUI"""

    def __init__(self, driver: WebElement):
        LinkedInLogin.__init__(self)
        LinkedInLoginProperties.__init__(self)
        LinkedInLoginUI.__init__(self, driver)


class JobSearchWebsitePropertiesSwitcher(
    JobSearchWebsiteLinks,
    JobSearchWebsiteLoginProperties,
    JobSearchWebsiteLoginUI,
    UIMockWebsiteJobSearch,
):
    """_summary_: Inherits all properties from JobSearchWebsiteLinks,
    JobSearchWebsiteLoginProperties, JobSearchWebsiteLoginUI"""

    def __init__(self, driver: WebElement):
        JobSearchWebsiteLinks.__init__(self)
        JobSearchWebsiteLoginProperties.__init__(self)
        JobSearchWebsiteLoginUI.__init__(self, driver)
        UIMockWebsiteJobSearch.__init__(self, driver)


def use_determiner(
    determiner: str, driver: webdriver.Chrome
) -> LinkedInPropertiesSwitcher | JobSearchWebsitePropertiesSwitcher:
    """_summary_: method to use to switch witch properties you will use

    Args:
        determiner (str): LinkedIn or Other Websites
        driver (webdriver.Chrome): driver you pass to collect elements

    Returns:
        LinkedInPropertiesSwitcher: an instance of LinkedIn properties and methods
        JobSearchWebsitePropertiesSwitcher: an instance of mock job website
            properties and methods

    Raises:
        ValueError: if determiner does not include within the dictionary
    """
    determiner_actions = {
        "LinkedIn": LinkedInPropertiesSwitcher,
        "Mock Website": JobSearchWebsitePropertiesSwitcher,
        # Add more determiners and methods as needed
    }
    action = determiner_actions.get(determiner)

    if action:
        return action(driver)
    raise ValueError(f"determiner {determiner} does not exist as an option")


"""This method is only to be used if element xpath is very flexible, and inherited 
    object is very flexible that this xpath method needs to be used instead"""


def get_element_xpath(xpath: str, driver: webdriver.Chrome) -> WebElement:
    """_summary_: method to use to get element xpath with inherited
        classes that do not have element properties

    Args:
        xpath (str): xpath as basis to find web element
        driver (webdriver.Chrome): driver that orchestrates the automation

    Returns:
        WebElement: Web Element retrieved
    """
    return driver.find_element(By.XPATH, xpath)
