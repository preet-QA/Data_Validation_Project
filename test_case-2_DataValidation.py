"""
# TestCase 2 = Function To check duplicate data values  in the columns
"""

import pytest

import pandas as pd


def test_check_duplicate_entries_in_columns():
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

    print(f"Columns : {duplicate_entry}  --> have duplicate entries")
    print(f"Columns : {unique_entry}  --> have unique entries")
    assert 'title' not in duplicate_entry ,"Test failed as 'title/product name' column has duplicate data"
    # If 'Title' has duplicate value then test wil fail







