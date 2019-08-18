import re

# ######################################################################
# Group Method, re module
#


def bare_delin():
    print(9 * '--------')


def ex_heading(ex_name):
    delin = 9 * '--------'
    print(f'\n{ex_name}\n{delin}')
# ######################################################################


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


# Print heading
# ######################################################################
bare_delin()
print('Group Method, re module')
print_pattern = """Regular expression to match:
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
"""
print(f'\nContent to parse (urls):{urls}')
print(print_pattern)
bare_delin()


# 1. Typical match with return from finditer method
# ######################################################################
ex_heading('Normal matching to a regular expression using finditer')

matches = pattern.finditer(urls)

for match in matches:
    print(match)

# ######################################################################
#
# The above match object has a 'group' method
#   the group method uses zero based indexing
#   to access the different groups (defined in
#   parentheses)
#
#   Group zero match.group(0) = entire match
#       object
#   Group one match.group(1) = first parenthetically
#       grouped content the optional 'www.'
#
# ######################################################################


# 2. Match group zero
# ######################################################################
bare_delin()
ex_heading('Matching to group(0) of a regular expression')

matches_0 = pattern.finditer(urls)

for match_0 in matches_0:
    print(match_0.group(0))     # group(0) = entire match


# 3. Match group one
# ######################################################################
bare_delin()
ex_heading('Matching to group(1) of a regular expression')

matches_1 = pattern.finditer(urls)

for match_1 in matches_1:
    print(match_1.group(1))


# 4. Match group two
# ######################################################################
bare_delin()
ex_heading('Matching to group(2) of a regular expression')

matches_2 = pattern.finditer(urls)

for match_2 in matches_2:
    print(match_2.group(2))


# 5. Match group three
# ######################################################################
bare_delin()
ex_heading('Matching to group(3) of a regular expression')

matches_3 = pattern.finditer(urls)

for match_3 in matches_3:
    print(match_3.group(3))


# Back Reference at 44:12
# ######################################################################
#
# RE module has a sub method (back reference) that can be used
#   to perform substitution.
# Format:
#   subbed_urls = pattern.sub(r'\2\3')
# Where:
#   subbed_urls is a variable to accept substituted values
#   pattern.sub() calls the sub() method
#   pattern.sub(r'\2\3') tells python which group by index
#   pattern.sub(r'\2\3', urls) 'urls' tells python text to searh
#
# ######################################################################

bare_delin()
ex_heading('Back reference with the sub() method')

subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

subbed_urls_1 = pattern.sub(r'\1\3', urls)
print(subbed_urls_1)