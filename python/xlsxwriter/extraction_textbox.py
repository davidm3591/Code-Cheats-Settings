import xlsxwriter

# #### XlsxWriter.pdf # ####
# #### Insert Textboxes into a Worksheet - pg 410 #### #

# Data for Extraction Sheet
# Title and leading text are bold
#
# Create format object for bold text - haven't figured
#   out how to add cell notation to text box (if possible)
# bold = workbook.add_format({'bold', True})
#
# REVIEW CRITERIA
# Speaker Rate/Flow:  Does the teacher speak in a natural pace that is appropriate for video?
# Speaker Presentation: Does the teacher make adequate use of the pen tool to draw students attention in to the lesson?
# Lesson flow: Do the ideas transition seamlessly from one to the next?  Are the Lesson Questions supported with appropriate detail that reinforce the big idea?
# Mistakes/Misspeaks: Are there any misspeaks or mistakes that will lead to student's learning inaccurate information?
# Content errors on slides or in spoken information:  Does the information on the slide match what the teacher is saying?
# Production Issues: Are there any issues with the quality of the video regarding audio or video,  clothing selection, etc.?

workbook = xlsxwriter.Workbook('extraction_textbox.xlsx')
worksheet = workbook.add_worksheet('textbox_demo')


text = "REVIEW CRITERIA\n"
text += "Speaker Rate/Flow:  Does the teacher speak in a natural pace that is appropriate for video?\n"
text += "Speaker Presentation: Does the teacher make adequate use of the pen tool to draw students attention in to the lesson?\n"
text += "Lesson flow: Do the ideas transition seamlessly from one to the next?  Are the Lesson Questions supported with\n"
text += 23 * " " + "appropriate detail that reinforce the big idea?\n"
# text += "appropriate detail that reinforce the big idea?\n"
# text += "                       appropriate detail that reinforce the big idea?\n"
text += "Mistakes/Misspeaks: Are there any misspeaks or mistakes that will lead to student's learning inaccurate information?\n"
text += "Content errors on slides or in spoken information:  Does the information on the slide match what the teacher is saying?\n"
text += "Production Issues: Are there any issues with the quality of the video regarding audio or video,  clothing selection, etc.?"

options = {
    'width': 785,
    'height': 165,
    'x-offset': 10,
    'y-offset': 10,
    'text_wrap': False,
    'align': {'vertical': 'top',
              'horizontal': 'left'
              },
}

worksheet.insert_textbox('B2', text, options)

workbook.close()
