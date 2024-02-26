"""Python file to return different web drivers"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


def chromedriver_setup():
    """_summary_: returns an instance of Chrome driver.

    Returns:
        webdriver.Chrome: A chrome driver instance
    """
    # start_display()
    # chromedriver_autoinstaller.install()
    chrome_options = add_chrome_options()
    return webdriver.Chrome(options=chrome_options)
    # return webdriver.Chrome()


def start_display():
    """_summary_: method to use to start display and returns a Display instance

    Returns:
        Display: a started display to chromedriver display
    """
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display


def get_webdriver_options():
    """_summary_: returns a list of webdriver options to be passed to shell

    Returns:
        list: a list that contains a string of setup to be enabled for webdriver.
    """
    return [
        # Define window size here
        "--window-size=1200,1200",
        "--ignore-certificate-errors",
        "--headless",
        # "--disable-gpu",
        # "--window-size=1920,1200",
        # "--ignore-certificate-errors",
        # "--disable-extensions",
        # "--no-sandbox",
        # "--disable-dev-shm-usage",
        #'--remote-debugging-port=9222'
    ]


def add_chrome_options():
    """_summary_: returns options to be used for chromedriver

    Returns:
        Options: an instance of Options where webdriver options are configured
    """
    chrome_options = Options()
    for option in get_webdriver_options():
        chrome_options.add_argument(option)
    return chrome_options
