# Build Python Switch statement

# ----------------------------------------------------------------------
# https://stackoverflow.com/questions/48200787/how-to-implement-the-switch-case-in-python
# def switch_demo(var):
#     switcher = {
#                 1: "Jan", 
#                 2: "Feb", 
#                 3: "March",
#                 4: "April", 
#                 5: "May", 
#                 6: "June", 
#                 7: "July", 
#                 8: "August", 
#                 9: "Sept", 
#                 10: "Oct", 
#                 11: "Nov", 
#                 12: "Dec"
#     }

    # return switcher.get(var,"Invalid Month")

# var = int(input("enter a number between 1 and 12:  "))
# print(switch_demo(var))
# ----------------------------------------------------------------------

# slide_type = switch_demo(var)
# print(slide_type)
# if "#video" in tags_result:
#             slide_type = "video"
#         elif "#rb" in tags_result: # change to = "radiobutton"
#             slide_type = "radiobutton"
#         elif "#cb" in tags_result:
#             slide_type = "checkbox"
#         elif "#fib" in tags_result:
#             slide_type = "fib"
#         elif "#dd" in tags_result:
#             slide_type = "dd"
#         elif "#html" in tags_result:
#             slide_type = "basic"
#         elif "#2cat" in tags_result:
#             slide_type = "Sort by Two Categories"
#         elif "#3cat"  in tags_result:
#             slide_type = "Sort by Three Categories"
#         elif "#rank"  in tags_result:
#             slide_type = "Ranking"
#         elif "#match"  in tags_result:
#             slide_type = "Matching"
#         elif "#int"  in tags_result:
#             slide_type = "Interactive"
#         elif "#te"  in tags_result:
#             slide_type = "Text Evidence"
#         else:
#             slide_type = ""

# s_t = input("Enter #tag_name:  ")
# def switch_slide_type(s_t):
#     slide_check = {
#                   "#rb": "radiobutton",
#                   "#cb": "checkbox",
#                   "#fib": "fib",
#                   "#dd": "dd",
#                   "#html": "basic",
#                   "#2cat": "Sort by Two Categories",
#                   "#3cat": "Sort by Three Categories",
#                   "#rank": "Ranking",
#                   "#match": "Matching",
#                   "#int": "Interactive",
#                   "#te": "Text Evidence",
#                   # "#": "",
#                   # "#": "",
#     }
#     return slide_check.get(s_t,"")

# slide_type = switch_slide_type(s_t)
# print(slide_type)

# Break in if statement
test_stop = input("Continue loop (y/n)? ")
test_stop = test_stop.lower()

if test_stop == 'y':
    pass
else:
    sys.exit(None)

tags_result = ["#rb"]
# tags_result.append()
def switch_slide_type(tags_result):
    slide_check = {
                  "#rb": "radiobutton",
                  "#cb": "checkbox",
                  "#fib": "fib",
                  "#dd": "dd",
                  "#html": "basic",
                  "#2cat": "Sort by Two Categories",
                  "#3cat": "Sort by Three Categories",
                  "#rank": "Ranking",
                  "#match": "Matching",
                  "#int": "Interactive",
                  "#te": "Text Evidence",
                  # "#": "",
                  # "#": "",
    }
    return slide_check.get(tags_result,"")

slide_type = switch_slide_type(*tags_result)
print(slide_type)