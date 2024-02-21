"""_summary_: LinkInterface interface class"""

from abc import ABC, abstractmethod


class LinkInterface(ABC):
    """_summary_: Interface class for Links"""

    @property
    @abstractmethod
    def web_link(self):
        """_summary_: get method property for web_link"""

    @web_link.setter
    @abstractmethod
    def web_link(self, url: str):
        """_summary_: setter method property for web_link

        Args:
            url (str): a url string to the website
        """
