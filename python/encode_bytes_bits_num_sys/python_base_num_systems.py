# ######################################################################
#
# Numbering systems and Python
#

#
# Common Numbering Systems
#   Binary: base 2
#   Octal: base 8
#   Hexadecimal (hex): base 16
#

#
# Converting string to int()
#   Python int() contructor assumes base 10 unless explicitly stated
#   Using "base" allows explicit declaration of system base value
#

# Example:

# Default is decimal (base 10)
default_base = int('11')        # Returns 11 (base 10), default
print(default_base)

# Decimal, explicit
base_10 = int('11', base=10)    # Returns 11 with base 10
print(base_10)

# Binary, explicit
base_2 = int('11', base=2)      # Returns 3 with base 2
print(base_2)

# Octal, explicit
base_8 = int('11', base=8)      # Returns 9 with base 8
print(base_8)

# Hex
base_16 = int('11', base=16)    # Returns 17 with base 16
print(base_16)


#
# Common Numbering Systems Literal Form
#   Binary literal: 0b or 0B - Example 0b11
#   Octal literal: 0o or 0O - Example 0o11
#   Hexadecimal (hex) literal: 0x or 0X - Example 0x11
#

# Example:

# Binary
print(0b11)

# Octal
print(0o11)

# Hex
print(0x11)

x = b"r\xc3\xa9sum\xc3\xa9" .decode("utf-8")
print(x)

import locale

y = locale.getpreferredencoding()   # returns cp1252
print(y)
