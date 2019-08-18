import xlsxwriter

# ######################################################################
#
# #### XlsxWriter.pdf # ####
# #### Conditional Formatting - pg 358 #### #
#

# Valid Input Values:
# RFP (Green)
# Add fill color, format 1 - RFP (Green)
# RGB: 5, 199, 19 Hex: #05C713
#
# 2nd Review (Yellow/orange)
# Add fill color, format 2 - 2nd Review (Yellow/orange)
# RGB: 250, 221, 6  Hex: #FADD06
#
# RESHOOT (Red)
# Add fill color, format 3 - RESHOOT (Red)
# RGB: 2: 215, 89, 89 Hex: #D75959

workbook1 = xlsxwriter.Workbook('extract_cond_format.xlsx')
worksheet1 = workbook1.add_worksheet()

worksheet1.set_column('B:B', 15)
# worksheet1.set_column('A:A', 30)
format_1 = workbook1.add_format({'bg_color': '#05C713',
                                 'font_color': '#000000'})
format_2 = workbook1.add_format({'bg_color': '#FADD06',
                                 'font_color': '#000000'})
format_3 = workbook1.add_format({'bg_color': '#D75959',
                                 'font_color': '#000000'})

# data = ['RFP', '2nd Review', 'RESHOOT']
caption = ('Cells with values >= 50 are in light-red.'
           'Values < 50 are in light-green.')

# Write the data
worksheet1.write('A1', caption)
worksheet1.write('B5', 'RFP')
worksheet1.write('B6', '2nd Review')
worksheet1.write('B7', 'RESHOOT')


# conditional format over
worksheet1.conditional_format('B5:K7', {'type': 'cell',
                                        'criteria': 'equal to',
                                        'value': '"RFP"',
                                        'format': format_1})

# Write another conditional format over the same range
worksheet1.conditional_format('B5:K7', {'type': 'cell',
                                        'criteria': 'equal to',
                                        'value': '"2nd Review"',
                                        'format': format_2})

# Write another conditional format over the same range
worksheet1.conditional_format('B5:K7', {'type': 'cell',
                                        'criteria': 'equal to',
                                        'value': '"RESHOOT"',
                                        'format': format_3})


workbook1.close()

# worksheet.conditional_format('A1', {'type':     'cell',
#                                     'criteria': 'equal to',
#                                     'value':    '"X"',
#                                     'format':   format1})
# row_count = 5
# # range(count)
# for num in range(count):
#     print(num)
# Sample data to run conditional formatting against.
# data = [
#     [34, 72, 38, 30, 75, 48, 75, 66, 84, 86],
#     [6, 24, 1, 84, 54, 62, 60, 3, 26, 59],
#     [28, 79, 97, 13, 85, 93, 93, 22, 5, 14],
#     [27, 71, 40, 17, 18, 79, 90, 93, 29, 47],
#     [88, 25, 33, 23, 67, 1, 59, 79, 47, 36],
#     [24, 100, 20, 88, 29, 33, 38, 54, 54, 88],
#     [6, 57, 88, 28, 10, 26, 37, 7, 41, 48],
#     [52, 78, 1, 96, 26, 45, 47, 33, 96, 36],
#     [60, 54, 81, 66, 81, 90, 80, 93, 12, 55],
#     [70, 5, 46, 14, 71, 19, 66, 36, 41, 21],
# ]

# ######################################################################
#
# XlsxWriter.pdf
# Example 1
#
