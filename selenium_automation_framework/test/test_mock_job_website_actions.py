"""Imports Mock Job Website Actions and chromedriver"""

from ..objects.job_search_result import JobSearchResult
from ..webdriver_setup.driver_setup import chromedriver_setup
from ..package.mock_job_website_actions import MockJobWebsiteActions
from .test_helpers import TestHelpers


def test_mock_website_login():
    """_summary_: tests that framework is able to login using the mock website"""
    # sets up driver and mock website actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    mock_website_actions = TestHelpers.login_actions(mock_website_actions)

    # asserts that user is able to login
    assert (
        mock_website_actions.properties.driver.current_url
        != mock_website_actions.properties.login_url()
    )

    mock_website_actions.properties.driver.quit()


def test_login_ui_get_set():
    """_summary_: tests that login_ui_interface is able to return different web elements"""
    # sets up driver and linkedIn actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    # assert is inside the login_ui_get_set() method
    TestHelpers.login_ui_get_set(
        instance=mock_website_actions,
        username_xpath='//*[text()="Username"]',
        password_xpath='//*[text()="Password"]',
        login_button_xpath='//*[text()="Forgot login info?"]',
    )

    mock_website_actions.properties.driver.quit()


def test_ui_job_search():
    """_summary_: tests that ui_job_search is able to search inb mock website"""
    # sets up driver and mock website actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    mock_website_actions = TestHelpers.ui_job_search(mock_website_actions, "Help Desk")
    assert mock_website_actions.properties.results_search_text_element.is_displayed()

    mock_website_actions.properties.driver.quit()


def test_ui_job_results():
    """_summary_: tests that ui_job_results is able to extract job results from website"""
    # sets up driver and mock website actions instance
    mock_website_actions = MockJobWebsiteActions(chromedriver_setup())
    mock_website_actions = TestHelpers.ui_job_search(mock_website_actions, "Help Desk")

    # stores job results to prepare for checking
    job_results: list[JobSearchResult] = mock_website_actions.store_job_results()

    # asserts that job results have four items
    # checks that items properties (except for date_posted) is not empty/None
