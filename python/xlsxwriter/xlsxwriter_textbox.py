import xlsxwriter

# #### XlsxWriter.pdf # ####

# #### Insert Textboxes into a Worksheet - pg 410 #### #

workbook = xlsxwriter.Workbook('textbox.xlsx')
worksheet = workbook.add_worksheet('textbox_demo')

# From PDF
text = 'Formatted textbox'
options = {
    'width': 980,
    'height': 150,
    'x-offset': 10,
    'y-offset': 10,
    'text_wrap': False,
    'align': {'vertical': 'top',
              'horizontal': 'left'
              },

    'font': {'size': 10},
    'font': {'color': 'red',
             'size': 14},
    'align': {'vertical': 'top',
              'horizontal': 'left'
              },
    'align': {'vertical': 'middle',
              'horizontal': 'center'
              },
    'gradient': {'colors': ['#DDEBCF'
                            '#9CB86E',
                            '#156B13']},
}

worksheet.insert_textbox('B2', text, options)

workbook.close()
