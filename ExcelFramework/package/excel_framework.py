# Module providing openpyxl extensions for framework
from openpyxl import Workbook, load_workbook


class ExcelFramework:
    """AI is creating summary for"""

    def __init__(self, filename=None):
        """__init__ declaration for objects

        Args:
            filename (_ZipFileFileProtocol, optional): filename of the file. Defaults to None.
        """
        if filename:
            self.workbook = load_workbook(filename)
        else:
            self.workbook = Workbook()
            self.workbook.create_sheet("Sheet1")

    def add_data(self, sheet_name, data, start_row=1, start_column=1):
        """Adds data to excel.

        Args:
            sheet_name (string): name of the sheet name for the data to be added on
            data (list): the following data to be added in the excel file, in list format.
            start_row (int, optional): row number to start putting data on. Defaults to 1.
            start_column (int, optional): column number to start putting data on. Defaults to 1.
        """
        sheet = self.workbook[sheet_name]
        for row_index, row_data in enumerate(data, start=start_row):
            for col_index, cell_data in enumerate(row_data, start=start_column):
                sheet.cell(row=row_index, column=col_index, value=cell_data)

    def save_workbook(self, filename):
        """save_workbook AI is creating summary for save_workbook

        Args:
            filename (_ZipFileFileProtocol): filename of the file.
        """
        self.workbook.save(filename)

    def load_workbook(self, filename):
        """
        load_workbook: method to use when loading an Excel Filename

        Args:
            filename (_ZipFileFileProtocol): filename of the file.
        """
        self.workbook = load_workbook(filename)
    
    def cell_is_not_empty(self, sheet_name, cell_name):
        sheet = self.workbook[sheet_name]
        cell = sheet[cell_name]
        return cell.value is not None

    # def add_data_to_empty_cell_with_existing_workbook(self, sheet_name, data):
    #     sheet = self.workbook[sheet_name]
    #     for row_index, row_data in enumerate(data, start=1):
    #         for col_index, cell_data in enumerate(row_data, start=1):
    #             sheet.a
