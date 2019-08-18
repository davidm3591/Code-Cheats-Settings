from datetime import date, time
import xlsxwriter

# #### XlsxWriter.pdf # ####

# #### Data Validation and DDs - pg 354 #### #

# Copy workbook and worksheet setup from pdf
workbook = xlsxwriter.Workbook('extract_dd_valid.xlsx')
# Create worksheet for dd testing
worksheet = workbook.add_worksheet('data_validation')

# Add format object for header (from pdf)
header_format = workbook.add_format({
    'border': 1,
    'bg_color': '#C6EFCE',
    'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',
    'indent': 1,
})

# Set up layout of worksheet (from pdf)
worksheet.set_column('A:A', 68)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_row(0, 36)

text = 'Drop Down Below'

worksheet.write('B2', text)
worksheet.data_validation('B3', {'validate': 'list',
                                 'source': ['---', 'RFP', '2nd Review', 'RESHOOT']})

workbook.close()
