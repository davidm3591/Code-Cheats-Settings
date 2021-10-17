""" Common Code Helps for Python Classes and Tutorials """

sep_mark = "\n<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--"
sep_mark += "<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>\n"
plain_sep_mark = "\n------------------------------------------------"
plain_sep_mark += "----------------------------------------------\n"

def output_sep_title(title):
    """ 
        prints out the seperation marker sep_mark
        prints out title as received as argument
    """
    print(f"{sep_mark}\t{title}{sep_mark}")

def output_sep_mark():
    """prints out the seperation marker sep_mark"""
    print(sep_mark)


def output_plain_sep_title(title):
    """ 
        prints out the plain seperation marker sep_mark
        prints out title as received as argument
    """
    print(f"{plain_sep_mark}\t{title}{plain_sep_mark}")

def output_plain_sep_mark():
    """prints out the plain seperation marker sep_mark"""
    print(plain_sep_mark)