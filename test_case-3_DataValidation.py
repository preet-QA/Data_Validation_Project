"""
# TestCase 3 = Function To check missing/extra columns in Extracted data file
"""
import pytest

import pandas as pd

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