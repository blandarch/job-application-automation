"""Imports LinkInterface class"""

from selenium_automation_framework.interfaces.links.link_interface import LinkInterface


class LinkedInLogin(LinkInterface):
    """_summary_: Inherits link_interface to provide link to LinkedIn Login."""

    def __init__(self):
        self.web_link = "https://www.linkedin.com/login"

    @property
    def web_link(self):
        return self.web_link

    @web_link.setter
    def web_link(self, url: str):
        self.web_link = url
