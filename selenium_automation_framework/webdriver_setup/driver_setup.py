"""Python file to return different web drivers"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# from webdriver_manager.chrome import ChromeDriverManager


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
    display = Display(visible=0, size=(800, 800))
    display.start()
    return display


def get_webdriver_options():
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
    chrome_options = Options()
    for option in get_webdriver_options():
        chrome_options.add_argument(option)
    return chrome_options


# def get_chrome_service():
#     return Service(ChromeDriverManager(chrome_type=))
