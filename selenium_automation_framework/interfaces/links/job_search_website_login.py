"""Imports LinkInterface class"""

from .link_interface import LinkInterface


class JobSearchWebsiteLinks(LinkInterface):
    """_summary_: Inherits link_interface to provide link to mock job search website Login."""

    def __init__(self):
        super().__init__(url="https://demo.jobboardmount.com/")

    def login_url(self, subdomain: str = "main/static/signIn"):
        return super().login_url(subdomain)
