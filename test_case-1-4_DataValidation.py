"""
This program is to validate the CSV file that contains extracted data
TestCase 1 = Function To check number of columns in Extracted data file
"""
import pytest

import pandas as pd


@pytest.mark.smoke
def test_check_total_columns():
    df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")
    column_name_list_expected = ("url", "brand", "title", "unit_price", "stock_count", "overview", "information", "manufacturer", "manufacturer_part", "tariff_number", "origin_country", "files", "file_urls", "image_urls","primary_image_url", "associated_parts", "trail")

    df = df.sample(n=5)
    # Retrieving number of columns in the csv file
    column_name_list = dict(df.dtypes)
    column_name_list_extracted_data = list(column_name_list.keys())
    print(f"Number of columns present in extracted data file : {len (column_name_list_extracted_data)}")
    print(f"Number of columns expected in data file : {len (column_name_list_expected)}")

    # Compare number of columns in extracted data file with expected number of columns
    if len(column_name_list_expected) == len(column_name_list_extracted_data):
        print(f"The number of columns in extracted csv is : {len (column_name_list_extracted_data)} and is matching with expected number of columns")
    else:
        print("There is mismatch in number of columns")
    missing_columns= len(column_name_list_expected)-len(column_name_list_extracted_data)

    if missing_columns >= 1: # validation if the number of columns are extra or missing as compared to expected columns
        print (f"Number of columns missing in extracted csv : {abs(missing_columns)}")
    elif missing_columns < 0:
        print (f"Number of columns extra in extracted csv : {abs(missing_columns)}")
    else:
        pass
    assert len(column_name_list_expected) == len(column_name_list_extracted_data), "Test failed as the column count doesnt match"
    # Test will fail if counts of expected column doesnt match with count of columns from extracted data


"""
# TestCase 2 = Function To check duplicate data values  in the columns
"""


def test_check_duplicate_entries_in_columns():
    # read the file
    df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")

    column_name_list = dict(df.dtypes)
    df = df.sample(n=5)

    # Defining 2 empty list to get column names wih duplicate entry
    duplicate_entry = []
    unique_entry = []
    for index in column_name_list:
        if (df[index].nunique()) > 2:  # retrieves the count of unique data
            duplicate_entry.append(index)  # if the data is repeating,column name is added to duplicate_entry list

        else:  # else column name is added to unique_entry list
            unique_entry.append(index)

    print(f"Columns : {duplicate_entry}  --> have duplicate entries")  # print columns with duplicate entries
    print(f"Columns : {unique_entry}  --> have unique entries")  # print columns with unique entries
    assert 'title' not in duplicate_entry ,"Test failed as 'title/product name' column has duplicate data"
    # Test will fail if ,'Title' has duplicate value


"""
# TestCase 3 = Function To check missing/extra columns in Extracted data file
"""


def test_check_missing_columns_names():
    df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")
    column_name_list_expected = ("url", "brand", "title", "unit_price", "stock_count", "overview", "information", "manufacturer","manufacturer_part", "tariff_number", "origin_country", "files", "file_urls", "image_urls", "primary_image_url","associated_parts", "trail")
    column_name_list = dict(df.dtypes)
    df = df.sample(n=5)
    column_name_list_extracted_data = list(column_name_list.keys())
    if column_name_list_expected == column_name_list_extracted_data:
        print("All the expected columns names are present in the csv file")
    else:
        list_difference = [] # creating an empty list to get the column names
        for item in column_name_list_expected:
            if item not in column_name_list_extracted_data:
                list_difference.append(item)
        print("Below column names are not matched in the extracted csv file")
        print(list_difference)

        list_extra = []
        for item in column_name_list_extracted_data:
            if item not in column_name_list_expected:
                list_extra.append(item)
        print("Below column names are extra in the extracted csv file(these column/s are not found in expected column list)")
        print(list_extra)

        print(f"column_names in extracted_data : {sorted(column_name_list_extracted_data)} ")
        print(f"Expected column_names: {sorted(column_name_list_expected)} ")
    assert column_name_list_expected == column_name_list_extracted_data , "Test Failed as some column names are missing)"


"""
TestCase 4 = Function To check missing values in columns in Extracted data file
"""


def test_check_missing_values():
    # read the csv file from location mentioned below
    df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")
    column_name_list = dict(df.dtypes)
    column_name_list_extracted_data = list(column_name_list.keys()) # get the list of columns from csv file
    df = df.sample(n=5)

    missing_entry_columns = []  # declare empty list to store missing entry columns
    all_data_present_columns = []  # declare empty list to store columns that have all data populated

    for index in column_name_list_extracted_data:
        if (df[index].isnull().values.any()):  # validation for column value is NULL
            missing_entry_columns.append(index)
        else:
            all_data_present_columns.append(index)
    print(f"Columns : {missing_entry_columns}  --> missing data for some rows")
    print(f"Columns : {all_data_present_columns}  --> data is present for all the rows")

    assert missing_entry_columns == [] , "Test failed as data is missing for some columns"
    # Test will fail if there are any missing entries for column


