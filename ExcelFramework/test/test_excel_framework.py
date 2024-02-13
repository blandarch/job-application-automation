""" Modules Needed to Test Excel Framework """

import os
import json
import traceback
from .static_constants import (
    ADD_DATA_WITH_FILENAME,
    SHEET_NAME,
    DATA_TO_INPUT,
    SAVE_FILENAME,
    ADD_DATA_WITHOUT_FILENAME,
    ADD_DATA_WITHOUT_FILENAME_ERROR,
    OPEN_FILENAME,
    EXPECTED_OUTPUT_FILENAME,
    ADD_DATA_WITH_FILENAME_ERROR,
    ADD_DATA_EMPTY_ROW_CELL_ERROR,
    ADD_DATA_EMPTY_ROW_CELL,
)
from .test_helpers import TestHelpers

CURRENT_DIRECTORY = os.getcwd()

with open("ExcelFramework/test/data.json", encoding="utf-8") as file:
    data = json.load(file)


def test_add_data_without_filename():
    """_summary_: checks validation on add_data using Without Filename"""

    try:
        # Adds data from empty excel file and saves it
        TestHelpers.create_workbook(
            data[ADD_DATA_WITHOUT_FILENAME][SHEET_NAME],
            data[ADD_DATA_WITHOUT_FILENAME][DATA_TO_INPUT],
            data[ADD_DATA_WITHOUT_FILENAME][SAVE_FILENAME],
        )

        # Asserts the produced excel file is equal to true
        assert TestHelpers.validate_excel_files(
            data[ADD_DATA_WITHOUT_FILENAME][SAVE_FILENAME],
            CURRENT_DIRECTORY
            + data[ADD_DATA_WITHOUT_FILENAME][EXPECTED_OUTPUT_FILENAME],
        ) == (True, "Excel files are equal.")

    except FileNotFoundError as error:
        print(ADD_DATA_WITHOUT_FILENAME_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    except AssertionError as error:
        print(ADD_DATA_WITHOUT_FILENAME_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    finally:
        # deletes sample file
        TestHelpers.delete_file(data[ADD_DATA_WITHOUT_FILENAME][SAVE_FILENAME])


def test_add_data_with_existing_filename():
    """_summary_: checks validation on add_data using With Filename"""
    try:
        # Adds data from empty excel file and saves it
        TestHelpers.create_workbook(
            data[ADD_DATA_WITH_FILENAME][SHEET_NAME],
            data[ADD_DATA_WITH_FILENAME][DATA_TO_INPUT],
            data[ADD_DATA_WITH_FILENAME][SAVE_FILENAME],
            CURRENT_DIRECTORY + data[ADD_DATA_WITH_FILENAME][OPEN_FILENAME],
        )

        # Asserts the produced excel file is equal to true
        assert TestHelpers.validate_excel_files(
            data[ADD_DATA_WITH_FILENAME][SAVE_FILENAME],
            CURRENT_DIRECTORY + data[ADD_DATA_WITH_FILENAME][EXPECTED_OUTPUT_FILENAME],
        ) == (True, "Excel files are equal.")

    except FileNotFoundError as error:
        print(ADD_DATA_WITH_FILENAME_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    except AssertionError as error:
        print(ADD_DATA_WITH_FILENAME_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    finally:
        # deletes file
        TestHelpers.delete_file(data[ADD_DATA_WITH_FILENAME][SAVE_FILENAME])


def test_add_data_to_empty_row_cell():
    """_summary_: checks validation of add_data_to_empty_row_cell"""
    try:
        # Adds data by inserting the nearest available row from the occupied rows
        TestHelpers.create_workbook_from_nearest_available_row(
            data[ADD_DATA_EMPTY_ROW_CELL][SHEET_NAME],
            data[ADD_DATA_EMPTY_ROW_CELL][DATA_TO_INPUT],
            data[ADD_DATA_EMPTY_ROW_CELL][SAVE_FILENAME],
            CURRENT_DIRECTORY + data[ADD_DATA_EMPTY_ROW_CELL][OPEN_FILENAME],
        )

        # Asserts the produced excel file is equal to true
        assert TestHelpers.validate_excel_files(
            data[ADD_DATA_EMPTY_ROW_CELL][SAVE_FILENAME],
            CURRENT_DIRECTORY + data[ADD_DATA_EMPTY_ROW_CELL][EXPECTED_OUTPUT_FILENAME],
        ) == (True, "Excel files are equal.")

    except FileNotFoundError as error:
        print(ADD_DATA_EMPTY_ROW_CELL_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    except AssertionError as error:
        print(ADD_DATA_EMPTY_ROW_CELL_ERROR.replace(r"{0}", str(error)))
        # Print the stack trace
        traceback.print_exc()

    finally:
        # deletes file
        TestHelpers.delete_file(data[ADD_DATA_EMPTY_ROW_CELL][SAVE_FILENAME])
