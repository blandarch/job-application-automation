"""Python file to return different web drivers"""

from selenium import webdriver


def chromedriver_setup():
    """_summary_: returns an instance of Chrome driver.

    Returns:
        webdriver.Chrome: A chrome driver instance
    """
    return webdriver.Chrome()
