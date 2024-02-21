"""Inherits WebElement, and Inheritances from parents properties"""

from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver

from selenium_automation_framework.interfaces.links.linkedin_login import LinkedInLogin
from selenium_automation_framework.interfaces.login_properties.linkedin_login_properties import (
    LinkedInLoginProperties,
)
from selenium_automation_framework.interfaces.login_UI.linkedin_login_ui import (
    LinkedInLoginUI,
)


def use_determiner(determiner: str, driver: webdriver.Chrome):
    """_summary_: method to use to switch witch properties you will use

    Args:
        determiner (str): LinkedIn or Other Websites
        driver (webdriver.Chrome): driver you pass to collect elements

    Raises:
        ValueError: if determiner does not include within the dictionary
    """
    determiner_actions = {
        "LinkedIn": LinkedInPropertiesSwitcher
        # Add more determiners and methods as needed
    }
    action = determiner_actions.get(determiner)

    if action:
        return action(driver)
    raise ValueError(f"determiner {determiner} does not exist as an option")


class LinkedInPropertiesSwitcher(
    LinkedInLogin, LinkedInLoginProperties, LinkedInLoginUI
):
    """_summary_: Inherits all properties from LinkedInLogin,
    LinkedInLoginProperties, LinkedInLoginUI"""

    def __init__(self, driver: WebElement):
        super(LinkedInLogin, self).__init__()
        super(LinkedInLoginProperties, self).__init__(driver)
        super(LinkedInLoginUI, self).__init__()
