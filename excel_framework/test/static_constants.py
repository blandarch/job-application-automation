"""Static Constants to be used for testing Excel Framework"""

# Validate Excel Files Strings
SHEET_NAMES_DIFFERENT = "Sheet names are different."
DIMENSIONS_SHEET_NAME_DIFFERENT = "Dimensions of sheet '{sheet_name}' are different."
CELL_IN_SHEET_NAME_DIFFERENT = "Cell in sheet is different."
EXCEL_FILES_EQUAL = "Excel files are equal."

# From data.json directory
ADD_DATA_WITHOUT_FILENAME = "addDataWithoutFilename"
ADD_DATA_WITH_FILENAME = "addDataWithFilename"
ADD_DATA_EMPTY_ROW_CELL = "addDataToEmptyRowCell"

SHEET_NAME = "sheetName"
DATA_TO_INPUT = "data"
OPEN_FILENAME = "openFilename"
SAVE_FILENAME = "saveFilename"
EXPECTED_OUTPUT_FILENAME = "expectedOutputFilename"

# Error Strings
ADD_DATA_WITHOUT_FILENAME_ERROR = (
    "method add_data_with_existing_filename_test error: {0}"
)
ADD_DATA_WITH_FILENAME_ERROR = "method add_data_with_existing_filename_test error: {0}"
ADD_DATA_EMPTY_ROW_CELL_ERROR = "method test_add_data_to_empty_row_cell error: {0}"
