"""Imports Action classes from package folder"""

from ..package.linkedin_actions import LinkedInActions
from ..package.mock_job_website_actions import MockJobWebsiteActions


class TestHelpers:
    """Test Helpers class for Selenium Automation Framework"""

    @staticmethod
    def login_actions(
        instance: LinkedInActions | MockJobWebsiteActions,
    ) -> LinkedInActions | MockJobWebsiteActions:
        """_summary_: method to call to test login actions from different websites in the framework

        Args:
            instance (LinkedInActions | MockJobWebsiteActions): instance of actions class
                from package folder

        Returns:
            LinkedInActions | MockJobWebsiteActions: an instance of action class from package folder
        """
        # gets username and password
        username, password = instance.properties.get_login_credentials()

        # logs in
        instance.go_to_login_page()
        instance.login(username, password)

        return instance

    @staticmethod
    def login_ui_get_set(
        instance: LinkedInActions | MockJobWebsiteActions,
        username_xpath: str,
        password_xpath: str,
        login_button_xpath: str,
    ):
        """_summary_: tests that login_ui_interface is able to return different web elements"""
        instance.go_to_login_page()

        # retrieves original elements for username, password and login
        original_username_element = instance.properties.username_element
        original_password_element = instance.properties.password_element
        original_login_element = instance.properties.login_button_element

        # passes different xpath for username, password, and login elements
        instance.properties.username_element = username_xpath
        instance.properties.password_element = password_xpath
        instance.properties.login_button_element = login_button_xpath

        # asserts that the original elements are different from the new elements inserted by xpath
        assert original_username_element != instance.properties.username_element
        assert original_password_element != instance.properties.password_element
        assert original_login_element != instance.properties.login_button_element

    @staticmethod
    def ui_job_search(
        instance: LinkedInActions | MockJobWebsiteActions, search_text: str
    ) -> LinkedInActions | MockJobWebsiteActions:
        """_summary_: method to go

        Args:
            instance (LinkedInActions | MockJobWebsiteActions): _description_
            search_text (str): _description_

        Returns:
            LinkedInActions | MockJobWebsiteActions: _description_
        """
        if isinstance(instance, MockJobWebsiteActions):
            instance.go_to_main_website()
        instance.search_jobs(search_text)

        return instance
