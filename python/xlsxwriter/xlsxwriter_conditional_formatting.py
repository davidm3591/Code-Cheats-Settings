import xlsxwriter

# ######################################################################
#
# #### XlsxWriter.pdf # ####
# #### Conditional Formatting - pg 358 #### #
#

# Valid Input Values:
#   RFP (Green)
#   2nd Review (Yellow/orange)
#   RESHOOT (Red)

workbook = xlsxwriter.Workbook('conditional_format.xlsx')
worksheet1 = workbook.add_worksheet('example_1')

# Add fill color, format 1
format_1 = workbook.add_format({'bg_color': '#FFC7CE',
                                'font_color': '#9C0006'})

# Add fill color, format 2
format_2 = workbook.add_format({'bg_color': '#C6EFCE',
                                'font_color': '#006100'})

# Sample data to run conditional formatting against.
data = [
    [34, 72, 38, 30, 75, 48, 75, 66, 84, 86],
    [6, 24, 1, 84, 54, 62, 60, 3, 26, 59],
    [28, 79, 97, 13, 85, 93, 93, 22, 5, 14],
    [27, 71, 40, 17, 18, 79, 90, 93, 29, 47],
    [88, 25, 33, 23, 67, 1, 59, 79, 47, 36],
    [24, 100, 20, 88, 29, 33, 38, 54, 54, 88],
    [6, 57, 88, 28, 10, 26, 37, 7, 41, 48],
    [52, 78, 1, 96, 26, 45, 47, 33, 96, 36],
    [60, 54, 81, 66, 81, 90, 80, 93, 12, 55],
    [70, 5, 46, 14, 71, 19, 66, 36, 41, 21],
]

# ######################################################################
#
# XlsxWriter.pdf
# Example 1
#
caption = ('Cells with values >= 50 are in light-red.'
           'Values < 50 are in light-green.')

# Write the data
worksheet1.write('A1', caption)

for row, row_data in enumerate(data):
    worksheet1.write_row(row + 2, 1, row_data)

worksheet1.conditional_format('B3:K12', {'type': 'cell',
                                         'criteria': '>=',
                                         'value': 50,
                                         'format': format_1})

# Write another conditional format over the same range
worksheet1.conditional_format('B3:K12', {'type': 'cell',
                                         'criteria': '<',
                                         'value': 50,
                                         'format': format_2})


workbook.close()
