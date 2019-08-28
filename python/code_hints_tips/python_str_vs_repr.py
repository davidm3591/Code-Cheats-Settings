# ######################################################################
#
# Python str() vs repr()
#
# ######################################################################


def brk_ln():
    print("")

# ###    str() vs repr()    ### #


# Example 1 of str()
str_intro = "Example 1 of str()"
print(str_intro)

s = "Hello, Geeks."
print(str(s))
print(str(2.0 / 11.0))

brk_ln()

# Example 1 of repr()
repr_intro = "Example 1 of repr()"
print(repr_intro)

s = "Hello, Geeks."
print(str(s))
print(str(2.0 / 11.0))
# -----------------------------------

brk_ln()


# Example 2 of str()
import datetime
today = datetime.datetime.now()

str_intro = "Example 2 of str()"
print(str_intro)

print(str(today))

brk_ln()

# Example 2 of repr()
repr_intro = "Example 2 of repr()"
print(repr_intro)

print(repr(today))
