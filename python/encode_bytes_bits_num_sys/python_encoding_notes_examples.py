# ######################################################################
#
# Encoding and Python
#

#
# Pick up pg 10 Unicode and & Character Encodings in Python:
#   A Painless Guide
#
#
#
#

#
# Follow up on Mojibake: https://en.wikipedia.org/wiki/Mojibake
#
#
#


# Python string Module - ASCII Character Set
# string Module Core
# ######################################################################
# From lib/python3.7/string.py

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

# the constants can be used for everyday string manipulation
# Example:
import string

s = "What's wrong with ASCII?!?!?!?!?"
print(s.rstrip(string.punctuation))
print(type(s))

print(string.printable)
print(string.punctuation)
print(str.isprintable(punctuation))
print(str.isprintable(whitespace))

# ######################################################################

# Stopped Pg 5 10/09/2019


a = b"r\xc3\xa9sum\xc3\xa9" .decode("utf-8")
print(a)

b = None


# Get OS native codec
# ######################################################################
import locale

y = locale.getpreferredencoding()
print(y)
# ######################################################################

# ######################################################################
# Scratchpad below here
# ######################################################################
# print(punctuation)
# print(printable)
