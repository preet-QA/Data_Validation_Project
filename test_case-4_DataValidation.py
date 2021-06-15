
"""
TestCase 4 = Function To check missing values in columns in Extracted data file
"""

import pytest

import pandas as pd

def test_check_missing_values():
    df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")
    column_name_list = dict(df.dtypes)
    column_name_list_extracted_data = list(column_name_list.keys())
    df = df.sample(n=5)

    missing_entry_columns = []
    all_data_present_columns = []

    for index in column_name_list_extracted_data:
        if (df[index].isnull().values.any()):
            missing_entry_columns.append(index)
        else:
            all_data_present_columns.append(index)
    print(f"Columns : {missing_entry_columns}  --> missing data for some rows")
    print(f"Columns : {all_data_present_columns}  --> data is present for all the rows")

    assert missing_entry_columns == [] , "Test failed as data is missing for some columns"