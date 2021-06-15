# Data_Validation_Project is to test the web scrapped data for Farnell spider
Automation TEST case (Created with pytest framework)
TestCase 1 = Function To check number of columnss in Extracted data file
TestCase 2 = Function To check duplicate data values  in the columns
TestCase 3 = Function To check missing/extra columns in Extracted data file
TestCase 4 = Function To check missing values in columns in Extracted data file
TestCase 5 = Function To check datatypes of columns in Extracted data file

filenames (Pytest):
test_case-1-4_DataValidation.py

filename(pycharm) :
test_case-5_DataValidation.py


Process to execute the files via command prompt
-Download the files at preferred location
-Go to that path via command prompt
-Run below command to execute the test cases and check status
py.test -k DataValidation -v -s

Programming language used: Python

