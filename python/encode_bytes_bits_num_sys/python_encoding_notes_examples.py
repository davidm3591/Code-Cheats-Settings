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

# Example:


a = b"r\xc3\xa9sum\xc3\xa9" .decode("utf-8")
print(a)

b = None

import locale

y = locale.getpreferredencoding()
print(y)