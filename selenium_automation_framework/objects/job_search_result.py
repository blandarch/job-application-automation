"""Job Search Result Object Class"""


class JobSearchResult:
    """Object class to store job results"""

    def __init__(
        self,
        job_title: str | None,
        job_description: str | None,
        company: str | None,
        date_posted: str | None,
    ):
        self._job_title: str = job_title
        self._job_description: str = job_description
        self._company: str = company
        self._date_posted: str = date_posted

    ###########################JOB TITLE################################
    @property
    def job_title(self) -> str:
        """_summary_: method to store job title

        Returns:
            str: job title in string
        """
        return self._job_title

    @job_title.setter
    def job_title(self, updated_job_title: str):
        self._job_title = updated_job_title

    ###########################JOB DESCRIPTION##########################
    @property
    def job_description(self) -> str:
        """_summary_: method to store job description

        Returns:
            str: job description in string format
        """
        return self._job_description

    @job_description.setter
    def job_description(self, updated_job_description: str):
        self._job_description = updated_job_description

    ###########################COMPANY##################################
    @property
    def company(self) -> str:
        """_summary_: method to store company name

        Returns:
            str: company name in string
        """
        return self._company

    @company.setter
    def company(self, updated_company: str):
        self._company = updated_company

    ###########################DATE POSTED##############################
    @property
    def date_posted(self) -> str:
        """_summary_: property to store when the job was posted in date

        Returns:
            str: str format of date
        """
        return self._date_posted

    @date_posted.setter
    def date_posted(self, updated_date_posted: str):
        self._date_posted = updated_date_posted
