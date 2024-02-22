"""Imports LinkInterface class"""

from .link_interface import LinkInterface


class LinkedInLogin(LinkInterface):
    """_summary_: Inherits link_interface to provide link to LinkedIn Login."""

    def __init__(self):
        super().__init__(url="https://www.linkedin.com/")
