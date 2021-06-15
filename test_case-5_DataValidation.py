"""
# TestCase 5 = Function To check datatypes of columns in Extracted data file
"""

import pandas as pd

from cerberus_list_schema import Validator

#Read the file
df = pd.read_csv("C://Preeti-sel//QA_DATA-validation_proj//web_scrapped_data.csv")
df = df.sample(n = 5)
df.head()

# create a schema for the columns based on the expected result
schema = {
    'url': {'type': 'string'},
    'brand': {'type': 'string'},
    'title': {'type': 'string'},
    'unit_price': {'type': 'integer'},
    'stock_count': {'type': 'integer'},
    'overview': {'type': 'string'},
    'information': {'type': 'string'},
    'manufacturer': {'type': 'string'},
    'manufacturer_part': {'type': 'string'},
    'tariff_number': {'type': 'string'},
    'origin_country': {'type': 'string'},
    'files': {'type': 'string'},
    'file_urls': {'type': 'string'},
    'image_urls': {'type': 'string'},
    'primary_image_url': {'type': 'string'},
    'associated_parts': {'type': 'string'},
    'trail': {'type': 'string'},
    }

v = Validator(schema)  # create an object of Validtor
df_dict = df.to_dict(orient='records')

error_dictionary = {}  # create an empty dictionary to store the errors
for index, record in enumerate(df_dict):
    if not v.validate(record):
        error_dictionary[index] = v.errors
error_list = (list (error_dictionary.values()))
# print(f"error list is : {error_list}")


def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        with open('datatype_error_in_column.txt', 'w') as writer:  # create a test file and open it in write mode
            writer.write("\n")  # Enter a new line
            writer.write(str(x))  # if the error is unique write it in excel

    print("Test execution is completed")
    print("Please check file 'datatype_error_in_column.txt' for datatype errors -(File location is same as script location)")


unique(error_list)