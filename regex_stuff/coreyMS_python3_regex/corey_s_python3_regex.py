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
print("\tTable of 'regex' Characters\n")

print(regex_chars)



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

sentence = 'Start a sentence and bring it to an end'


# Table of examples
example_defined = '''CHARACTERS FOR ALPHA-NUMERIC AND WHITESPACE AND INVERSES
Example #1: Simple literal string regex search, compiled, output finditer()
Example #2: Using the dot "." character - any character except new line - must\n\t\tescape to find a period
Example #3: "\d" character to match all digits (numeric characters)
Example #4: "\D" character to match all non-digits (non-numeric characters)
Example #5: "\w" - Word Character (a-z, A-Z, 0-9, _)
Example #6: "\s"  - Whitespace (space, tab, newline)

ANCHORS
Example #7: "\\b" - Word Boundary (white space or non alpha-numeric characters)
Example #8: "^" - Beginning of a String
Example #9: "$" - End of a String
Example #10:
Example #11:
'''
print()

# print the example block
output_plain_sep_mark()
print(example_defined)
output_plain_sep_mark()

# 
# Using 'r' to indicate to Python that this is a 'raw string'
# std_string = "\tTab"        # Python interprets \t as a tab space
# print(std_string)
# raw_string = r"\tTab"       # Python interprets \t as literal characters
# print(raw_string)
# 



# --------------------------------------------------------------- #

# Example 1
# 
# Simple search for literal characters matching 'abc'
# 
print("Example 1\nFind match for 'abc' using finditer() method\n")

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



# --------------------------------------------------------------- #

# Example 2
# 
# Using the dot "." character
# 

print("Example 2\nDot character, all except newline, escaped = period\n")

# Using . character unescaped
pattern = re.compile(r'.')    # Search for all alphanumeric except newline

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Unescaped:")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nUnescaped character finds stopped after 10 interations.')

print('\n')

# print("Escaped:")

pattern = re.compile(r'\.')    # Search for all alphanumeric except newline

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Escaped:")
for match in matches:
    print(f'\t{match}')


output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 3
# 
# Using "d" character to search for all digits (numeric characters)
# 

print("Example 3\n'd' character, all digits")

print()
# Using . character unescaped
pattern = re.compile(r'\d')    # Search for all alphanumeric except newline

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Numeric characters - d = digits:")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nNumeric character (digit) finds stopped after 10 interations.')


output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 4
# 
# Using "D" character to search for all non-digit (non-numeric characters)
# 

print("Example 4\n'D' character, all non-digits")

print()

pattern = re.compile(r'\D')    # Search for all alphanumeric except newline

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Numeric characters - D = non-digits:")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nNon-numeric character "D" finds stopped after 10 interations.')


output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 5
# 
# Using "w" character to search for all word characters a-z, A-Z, 0-9 & _
# 

print("Example 5\n'w' character, all word characters - a-z,\n\tA-Z, 0-9, & '_'")

print()

pattern = re.compile(r'\w')    # Search for all alphanumeric except newline

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Word characters - w = a-z,\n\tA-Z, 0-9, & '_':")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nNon-numeric character "D" finds stopped after 10 interations.')



# --------------------------------------------------------------- #
output_plain_sep_mark()

# Example 6
# 
# Using "s" to search for all whitespace - space, tab, newline
# 


print("Example 6\nUsing 's' to search for all whitespace - space, tab, newline")

print()

pattern = re.compile(r'\s')    # Search for all 

matches = pattern.finditer(text_to_search) # assign search result to a var

print("Whitespace locations:")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nWhitespace character "s" finds stopped after 10 interations.')

print()



# --------------------------------------------------------------- #
output_plain_sep_mark()

# Example 7
# 
# Using "\\b" Word Boundary (white space or non alpha-numeric characters)
# 

print("Example 7\nUsing the 'b' character to search for all words 'Ha' with a \n\tword boundary - whitespaceor  non-alpha-numeric")

print()

pattern = re.compile(r'\bHa')    # Search for all 

matches = pattern.finditer(text_to_search) # assign search result to a var

print("All words 'Ha' that have a word boundary 'b'")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print()



# --------------------------------------------------------------- #
output_plain_sep_mark()

# Example 8
# 
# Using "^" at the beginning (a word or character at the start)
# 

print("Example 8\nUsing the '^' character to search for words at the beginning of a sentence")

print()

pattern = re.compile(r'^Start')    # Search for all 

matches = pattern.finditer(sentence) # assign search result to a var

print("All words 'Start' that are at the beginning of sentence")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print()



# --------------------------------------------------------------- #
output_plain_sep_mark()

# Example 9
# 
# Using "$" at the end (a word or character at the end)
# 

print("Example 9\nUsing the '$' character to search for strings at the end of a sentence")

print()

pattern = re.compile(r'end$')    # Search for all 

matches = pattern.finditer(sentence) # assign search result to a var

print("All words 'end' that are at the end of sentence")
count = 1
for match in matches:
    if count <= 10:
        print(f'\t{match}')
        count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print()


# Stopped: 9:18

# Layout

output_plain_sep_mark()

# --------------------------------------------------------------- #
# output_plain_sep_mark()

# Example 5
# 
# Using "w" character to search for all word characters a-z, A-Z, 0-9 & _
# 

# print("Example 5\n'w' character, all word characters - a-z,\n\tA-Z, 0-9, & '_'")

# print()

# pattern = re.compile(r'\w')    # Search for all 

# matches = pattern.finditer(text_to_search) # assign search result to a var

# print("Word characters - w = a-z,\n\tA-Z, 0-9, & '_':")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nNon-numeric character "D" finds stopped after 10 interations.')


print()