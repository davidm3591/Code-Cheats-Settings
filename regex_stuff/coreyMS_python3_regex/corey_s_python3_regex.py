import re # standard Python regular expression module
from common_code_snips import *

# output_sep_title(title)
# output_sep_mark()
# 
# output_plain_sep_title(title)
# output_plain_sep_mark()

# https://www.youtube.com/watch?v=K8L6KVGG-7o"

def exercises(exercise_number):
    print(f'\nExercise # {exercise_number}')


exercise_defined = '''Exercise #1: Simple literal string regex search
Exercise #2: 
Exercise #3:
Exercise #4: 
Exercise #7:
Exercise #6: 
Exercise #3:
'''



output_plain_sep_title("Corey Schafer Regex: Python Tutorial: re Module\n\tHow to Write and Match Regular Expressions (Regex)")




regex_chars = '''.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

ANCHORS
\\b      - Word Boundary (white space or non alpha-numeric characters)
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)

Methods
.finditer()     - Iterates thru and returns match and index
                - <re.Match object; span=(1, 4), match='abc'>

#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
'''
print()
print("Table of 'regex' Characters")

print(regex_chars)

# output_plain_sep_mark()



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




output_plain_sep_mark()
print()
print("Unless otherwise specified, examples use the following data")

print()

sample_data = '''
text_to_search = 
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


sentence = 'Start a sentence and bring it to an end.'
'''
print(sample_data)

print()
output_plain_sep_mark()
print(exercise_defined)

output_plain_sep_mark()

# 
# Using 'r' to indicate to Python that this is a 'raw string'
# std_string = "\tTab"        # Python interprets \t as a tab space
# print(std_string)
# raw_string = r"\tTab"       # Python interprets \t as literal characters
# print(raw_string)
# 

exercises(1)
# 
# Simple search for literal characters matching 'abc'
# 
print("Find match for 'abc' using finditer() method\n")

# Using 'compile()' method allows assigning patterns to a variable
pattern = re.compile(r'abc')    # Search for literal characters & store in var

matches = pattern.finditer(text_to_search) # assign search result to a var

for match in matches:
    print(f'\t{match}')

print('\n')

# Using the index nums returned from using finditer() method
print("Locate match characters from findter() 'span=(1,4)'\nusing the index nums in text_to_search[1:4]:\n")

print(f'\t{text_to_search[1:4]}')

output_plain_sep_mark()
