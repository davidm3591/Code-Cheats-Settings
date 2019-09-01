#
# The Complete Unicode in Python Course
#

#
# Bash as console for python
#   To run python in bash
#   $ winpty python
#

#
# Using VIM to show unicode characters
#   Enter insert mode ctrl + "i"
#   Enter ctrl + "v", release and press lowercase "u"
#     (for character whose code point does not fit in
#      16 bits, use uppercase "U")
#   Enter the character's numerical (hexadecimal) unicode
#     value (code point)
#   To find numerical (hex) value of unicode character,
#     place cursor over character and press "GA"
#

#
# Unicode input and output on the Windows console
#   Python interpreter is limited in reading and
#   displaying Unicode characters (standard out can
#   only handle CP437)
#
# Package to workaround limitations
#   (NOTE:will crash in virtualenv):
#   pip install win-unicode-console
#   import win_unicode_console
#   win_unicode_console.enable()
#

euro = f'\u20ac'

print(euro)

some_val = ""


try:
    with open('/tmp/input.txt', 'r') as f:
        ...
except OSError:
    # 'File not found' error message.
    print("Fichier non trouvé")

"\N{GREEK CAPITAL LETTER DELTA}"  # Using the character name
'\u0394'
"\u0394"                          # Using a 16-bit hex value
'\u0394'
"\U00000394"                      # Using a 32-bit hex value
'\u0394'


b'\xE2\x82\xAC'.decode('UTF-8')
print(b'\xE2\x82\xAC'.decode('UTF-8'))

b'A' == b'\x41'

print(b'A' == b'\x41')

print(b'\x41')

# print(b'A')

# print(b'€'.encode('UTF-8'))

print(b'\x42')

print('\x42')

print('')
