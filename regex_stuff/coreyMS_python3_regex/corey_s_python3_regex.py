import re # standard Python regular expression module
from common_code_snips import *

# output_sep_title(title)
# output_sep_mark()
# 
# output_plain_sep_title(title)
# output_plain_sep_mark()

output_plain_sep_title(title)

# 
# text to search from: beginning_text_for_regex_cs.txt
# 

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and bring it to an end.'

# 
# Using 'r' to indicate to Python this is a 'raw string'
# 
# std_string = "\tTab"        # Python interprets \t as a tab space
# print(std_string)

# raw_string = r"\tTab"       # Python interprets \t as literal characters
# print(raw_string)


# 
# Using 'compile()' method allows assigning patterns to a variable
# 
pattern = re.compile(r'abc')    # Search for literal characters & store in var

matches = pattern.finditer(text_to_search) # assign search result to a var

for match in matches:
    print(match)

