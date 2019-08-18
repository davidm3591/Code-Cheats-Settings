import xlsxwriter
from datetime import datetime

# ######################################################################
# #######                Read The Docs Tutorials:                #######
# ####### https://xlsxwriter.readthedocs.io/getting_started.html #######
# ######################################################################

# ######################################################################
# #######          Tutorial I: Create a simple XLSX file         #######
# ######################################################################

# Build tuple of lists to populate worksheet
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)

# Create workbook - workbook takes one non-optional argument: name.xlsx
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
# The workbook object is used to add worksheet with add_worksheet() method
# add_worksheet takes one optional argument: worksheet name - default Sheet1
worksheet = workbook.add_worksheet()

# Start from the first cell (0,0)
row = 0
col = 0

# Iterate over data and write out row by row
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

# Close the workbook to create it
workbook.close()

# ######################################################################
# #######     Tutorial II: Adding formatting to the XLSX File    #######
# ######################################################################

workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet('Budget')

# Use format object to add bold and num_format
bold = workbook.add_format({'bold': True})
money = workbook.add_format({'num_format': '$#,##0'})

# Add some data headers
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

expenses_02 = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)


row = 1
col = 0

for item, cost in (expenses_02):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()


# ######################################################################
# ##### Tutorial III: Writing different types of data to XLSX File #####
# ######################################################################

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses03.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Add a number format for cells with money.
money_format = workbook.add_format({'num_format': '$#,##0'})

# Add an Excel date format.
date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

# Adjust the column width.
worksheet.set_column(1, 1, 15)

# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Date', bold)
worksheet.write('C1', 'Cost', bold)

# Some data we want to write to the worksheet.
expenses_03 = (
    ['Rent', '2013-01-13', 1000],
    ['Gas', '2013-01-14', 100],
    ['Food', '2013-01-16', 300],
    ['Gym', '2013-01-20', 50],
)

# Start from the first cell below the headers.
row = 1
col = 0

for item, date_str, cost in (expenses_03):
    # Convert the date string into a datetime object.
    date = datetime.strptime(date_str, "%Y-%m-%d")

    worksheet.write_string(row, col, item)
    worksheet.write_datetime(row, col + 1, date, date_format)
    worksheet.write_number(row, col + 2, cost, money_format)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

workbook.close()
