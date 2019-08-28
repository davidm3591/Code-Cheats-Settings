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
# 
# 
# 
#

# Example:


x = b"r\xc3\xa9sum\xc3\xa9" .decode("utf-8")
print(x)

import locale

y = locale.getpreferredencoding()
print(y)
