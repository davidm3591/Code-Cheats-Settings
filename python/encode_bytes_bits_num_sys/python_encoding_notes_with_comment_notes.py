# ######################################################################
#
# Unicode & Character Encodings in Python: A Painless Guide
# Advanced Python - Brad Solomon May 20, 2019
# https://realpython.com/python-encodings-guide/
#
#
course_info = """Unicode & Character Encodings in Python: A Painless Guide
Advanced Python - Brad Solomon May 20, 2019
https://realpython.com/python-encodings-guide/"""
#
#


def line_brk():
    print('\n')


fsnl = "\n"
intro_brk = 3 * "====================="
sec_brk = 3 * "---------------------"

print(intro_brk)
print(course_info)
print(intro_brk)
line_brk()
#
# Follow up on Mojibake: https://en.wikipedia.org/wiki/Mojibake
#
#
#


# ######################################################################
#
# Python string Module - ASCII Character Set
# 'string' Module Core
#
#
string_module = """
Python string Module - ASCII Character Set
string' Module Core
"""
print(f'{sec_brk}{string_module}{sec_brk}')
#
#

#
# From lib/python3.7/string.py
#
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace


#
# The constants can be used for everyday string manipulation
# Example:
#
import string

# Use constant 'punctuation' from 'string' module
s = "What's wrong with ASCII?!?!?!?!?"
print(
    f"This is using 's.rstrip(string.punctuation)' for the"
    f" 'punctuation' constant to strip{fsnl}the punctuation"
    f" from s = 'What is wrong with ASCII?!?!?!?!?'{fsnl}"
    f"   {s.rstrip(string.punctuation)}")

#
# Use constant 'whitespace' from 'string' module
#
line_brk()
print(
    f"This is using 'string.printable' for the"
    f"'printable' constant:{fsnl}   {string.printable}")

#
# Use constant 'whitespace' from 'string' module
#
line_brk()
print(
    f"This is using 'string.punctuation' for the"
    f"'punctuation' constant:{fsnl}   {string.punctuation}")

#
# Use constant 'whitespace' from 'string' module
#
line_brk()
print(
    f"This is using 'str.isprintable(punctuation)' for the"
    f"'punctuation' constant with the isprintable method."
    f" Return: {str.isprintable(punctuation)}")

#
# Use constant 'whitespace' from 'string' module
#
line_brk()
print(
    f"This is using 'str.isprintable(whitespace)' for the"
    f"'whitespace' constant with the isprintable method."
    f" Return: {str.isprintable(whitespace)}")

line_brk()
# ######################################################################
#
# Different Numbering Systems: Specifying and typing by literal form
# Using int() constructor to demo different numbering systems
#
#
num_sys = """
Different Numbering Systems: Specifying and typing by literal
form using int() constructor to demo different numbering systems
"""
print(f'{sec_brk}{num_sys}{sec_brk}')
#
#

#
# Base 10
#
test_base10 = int('11', base=10)
print(
    f"Using 'int('11', base=10)' for base 10 (decimal) representation "
    f"of the number 11:   {test_base10}")

#
# Base 2 - binary
#
test_base2 = int('11', base=2)
print(
    f"Using 'int('11', base=2)' for base 2 (binary) representation "
    f"of the number 11:   {test_base2}")

#
# Base 8 - octal
#
test_base8 = int('11', base=8)
print(
    f"Using 'int('11', base=8)' for base 8 (octal) representation "
    f"of the number 11:   {test_base8}")

#
# Base 16 - hex
#
test_base16 = int('11', base=16)
print(
    f"Using 'int('11', base=16)' for base 16 (hex) representation "
    f"of the number 11:   {test_base16}")

#
# Using Python literals to type integers
#
# Base 10 - base 10 is Python's default
#
line_brk()
print(
    f"Base 10 - base 10 is Python's default so there is not "
    f"literal to represent decimal")

line_brk()
print(
    f"Representing number 11 with binary, octal, and hex literals"
    f"{fsnl}Base 10 - base 10 is Python's default so there is not "
    f"literal to represent decimal"
    f"{fsnl}Number: 11 -- Prefix '0b' or '0B' -- Binary literal  '0b11': {0b11}"
    f"{fsnl}Number: 11 -- Prefix '0o' or '0O' -- Octal literal  '0o11': {0o11}"
    f"{fsnl}Number: 11 -- Prefix '0x' or '0x' -- Hex literal  '0x11': {0x11}")


#
# Get OS native codec
#
import locale

y = locale.getpreferredencoding()
print("\n")
print(
    f"Finding the OS preferred encoding using"
    f"'locale.getpreferredencoding()'{fsnl}"
    f">>> import locale{fsnl}"
    f">>> y = locale.getpreferredencoding(){fsnl}"
    f">>> print(y){fsnl}"
    f"{y}")
# ######################################################################
line_brk()
# ######################################################################
# Scratchpad below here
# ######################################################################
# print(punctuation)
# print(printable)

# Stopped Pg 5 10/09/2019
a = "résumé".encode('utf-8')
print(a)
b = b'r\xc3\xa9sum\xc3\xa9'.decode('utf-8')
print(b)                                        # doesn't work in ST build

c = "El Niño".encode("utf-8")
print(c)
d = b'El Ni\xc3\xb1o'.decode("utf-8")
print(d)                                        # doesn't work in ST build

# b = None

print(b'\xe1\x89\x88')
