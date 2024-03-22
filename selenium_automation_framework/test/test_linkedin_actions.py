"""Imports LinkedIn Actions and chromedriver"""

from ..webdriver_setup.driver_setup import chromedriver_setup
from ..package.linkedin_actions import LinkedInActions
from .test_helpers import TestHelpers
from ..objects.job_search_result import JobSearchResult


def test_linkedin_login():
    """_summary_: tests that framework is able to login using LinkedIn"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    linkedin_actions = TestHelpers.login_actions(linkedin_actions)

    # asserts that user is able to login
    assert (
        linkedin_actions.properties.driver.current_url
        != linkedin_actions.properties.login_url()
    )


def test_ui_get_set():
    """_summary_: tests that login_ui_interface is able to return different web elements"""
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    # assert is inside the login_ui_get_set() method
    TestHelpers.login_ui_get_set(
        instance=linkedin_actions,
        username_xpath='//label[contains(text(), "Email")]',
        password_xpath='//label[contains(text(), "Password")]',
        login_button_xpath='//*[contains(text(), "Forgot password?")]',
    )


def test_ui_job_search_and_store_result():
    # sets up driver and linkedIn actions instance
    linkedin_actions = LinkedInActions(chromedriver_setup())
    # signs in and tests Job Search
    linkedin_actions = TestHelpers.login_actions(linkedin_actions)
    linkedin_actions = TestHelpers.ui_job_search(linkedin_actions, "QA Engineer")
    # tests if it is able to produce job results and stores it in the object
    job_results: list[JobSearchResult] = linkedin_actions.store_job_results()

    # checks that items properties (except for date_posted) is not empty/None
    for job_result in job_results:
        assert len(job_result.job_title) != 0
        assert len(job_result.job_description) != 0
        assert len(job_result.company) != 0
        assert job_result.date_posted is None

    linkedin_actions.properties.driver.quit()
