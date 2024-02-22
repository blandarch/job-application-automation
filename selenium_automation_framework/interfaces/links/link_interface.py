"""_summary_: LinkInterface interface class"""


class LinkInterface:
    """_summary_: Interface class for Links"""

    def __init__(self, url: str):
        self._url = url

    @property
    def url(self):
        """_summary_: get method property for web_link"""
        return self._url

    @url.setter
    def url(self, url: str):
        self._url = url

    def login_url(self, subdomain: str = "login/"):
        """_summary_: method to retrieve login subdomain for url

        Args:
            subdomain (str): _description_

        Returns:
            _type_: _description_
        """
        return self._url + subdomain
