# import required libraries
import openpyxl
import csv
import pandas as pd

# open given workbook
# and store in excel object
excel = openpyxl.load_workbook("assets/test_files.xlsx")

# select the active sheet_3B
sheet_3B = excel["3B"]
sheet_3C = excel["3C"]

# writer object is created
col = csv.writer(open("assets/test_files.csv",
                      'w',
                      newline=""))
index = 1
# writing the data in csv file
for r in sheet_3B.rows:
    # row by row write
    # operation is perform
    if str(r[0].value) == 'None':
        continue
    if str(r[0].value) != 'No.':
        r[0].value = index
        index += 1
    col.writerow([cell.value for cell in r])

for r in sheet_3C.rows:
    # row by row write
    # operation is perform
    if str(r[0].value) == 'None' or str(r[0].value) == 'No.':
        continue
    r[0].value = index
    index += 1
    col.writerow([cell.value for cell in r])
# ---------------------------------------------------------------------------
# read the csv file and
# convert into dataframe object
# df = pd.DataFrame(pd.read_csv("assets/test_files.csv"))

# show the dataframe
# df
