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





output_plain_sep_title("Corey Schafer Regex: Python Tutorial: re Module\n\tHow to Write and Match Regular Expressions (Regex)\n\tRegex Applied - Practicle Examples")




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

pat
mat
cat
bat
fat
sat
'''

sentence = 'Start a sentence and bring it to an end.'


# Table of examples
example_defined = '''
Example #1: Using regex characters for phone number pattern - simple, explicit:\n\t    \d\d\d.\d\d\d.\d\d\d\d

Example #2: Parse & snag phone nums from an external text file - simple, explicit:\n\t    \d\d\d.\d\d\d.\d\d\d\d

Example #3: Parse & snag phone numss using a character set that sets delimiter\n\t     to "-" or "."

Example #4: 800 and 900 phone numbers with expanding the use of character sets

Example #5: Parse & snag data from an external text file expanding the use of character\n\t    sets to pull 800 & 900 numbers with delimiters "-" or "."

Example #6: Using ranges in charcter sets


Example #7: Using ^ as negation in a character set

Example #8: Using quantifiers to limit typing (and potential errors)

Example #9: Matching variable string content (Mr. Name, Mr Name Mrs. Name, Ms Name, etc)\n\t    by including quantifiers, and groups

Example #10: Matching emails

Example #11:
'''

print()

# print the example block
output_plain_sep_mark()
print("\tTABLE OF EXAMPLES - REGEX APPLIED")
print(example_defined)
output_plain_sep_mark()

print('\n')

# Example #3: Parse & snag phone numss using a character\n\t    set that sets delimiter to "-" or "."

# --------------------------------------------------------------- #
output_plain_sep_mark()

# Example 1
# 
# Use regex characters to find phone number pattern
# 

print("Example 1\nUse regex characters to find phone numbers")

print()

pattern_1 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')    # finding the first 3 digits

matches_1 = pattern_1.finditer(text_to_search) # assign search result to a var

print("All all phone numbers in 'text_to_search'")

for match in matches_1:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_1 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')")

output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 2
# 
# Parse & snag phone nums from an external text file
# 

print("Example 2\nUse regex characters to find phone numbers in an external text document")

print()

pattern_2 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

print("All phone numbers in external text file 'data.txt'")

count = 1

with open('data.txt', 'r') as f:
    contents = f.read()

    matches_2 = pattern_2.finditer(contents)

    for match in matches_2:
        if count <= 10:
            print(f'\t{match}')
            count += 1

print('\nPhone number finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_2 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')")


output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 3
# 
# Use regex characters to find phone number pattern and set delimiter
#   to either '-' or '.'
# 

print("Example 3\nUse regex characters to find phone numbers and use a 'character set [-.]'\n\tto set delimiter to '-' or '.' in data set 'text_to_search'")

print()

pattern_3 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

matches_3 = pattern_3.finditer(text_to_search) # assign search result to a var

print("All all phone numbers in 'text_to_search'")

for match in matches_3:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_3 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')")

output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 4
# 
# Use regex characters to find 800 or 900 phone number pattern expanding the use of character sets
# 

print("Example 4\nUse regex characters to find phone numbers and use a 'character set [-.]'\n\tto set delimiter to '-' or '.' and 'character set [89]' to find\n\tonly 800 and 900 numbers in data set 'text_to_search'")

print()

pattern_4 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')    # finding the first 3 digits

matches_4 = pattern_4.finditer(text_to_search) # assign search result to a var

print("All all 800 and 900 phone numbers in 'text_to_search'")

for match in matches_4:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_4 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')")

output_plain_sep_mark()



# --------------------------------------------------------------- #

# Example 5
# 
# Using character sets to parse & snag 800 and 900 phone nums from an 
#   external text file with delimiter characters '-' and '.'
# 

print("Example 5\nUse regex character sets to find 800 and 900 phone numbers with delimiters\n\tof - or . in an external text document")

print()

pattern_5 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

print("All 800 and 900 phone numbers with delimiter - and . in external text file 'data.txt'")

count = 1

with open('data.txt', 'r') as f:
    contents = f.read()

    matches_5 = pattern_5.finditer(contents)

    for match in matches_5:
        if count <= 10:
            print(f'\t{match}')
            count += 1

print('\nPhone number finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_5 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')")

output_plain_sep_mark()



# --------------------------------------------------------------- #


# Example 6
# 
# Using ranges in charcter sets
# 

print("Example 6\nUse regex ranges in character sets to find 'a-z' and 'A-Z'")

print()

pattern_6 = re.compile(r'[a-zA-Z]')    # finding the first 3 digits

matches_6 = pattern_6.finditer(text_to_search) # assign search result to a var

print("All letters in character sets a-z and A-B in 'text_to_search'")

count = 1
for match in matches_6:
    if count <= 10:
        print(f'\t{match}')
        count += 1

print('\nCharacters range finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_6 = re.compile(r'[a-zA-Z]')")

output_plain_sep_mark()



# --------------------------------------------------------------- #


# Example 7
# 
# Using ^ as negation character in a set
# 

print("Example 7\nUse regex ^ in character set to find all 3 letter words ending in _at except bat")

print()

pattern_7 = re.compile(r'[^b]at')    # finding the first 3 digits

matches_7 = pattern_7.finditer(text_to_search) # assign search result to a var

print("All 3 letter words ending in 'at' except bat in 'text_to_search'")

for match in matches_7:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_7 = re.compile(r'[^b]at')")

output_plain_sep_mark()



# --------------------------------------------------------------- #


# Example 8
# 
# Using quatifiers
# 

print("Example 8\nUse qutifiers to limit typing (and potential errors) using {n} - exact quantifier\n\t(n = a number in braces)")

print()

pattern_8 = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

matches_8 = pattern_8.finditer(text_to_search) # assign search result to a var

print("All phone numbers using {n} - exact quantifier (n = a number in braces)'")

for match in matches_8:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_8 = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')")

output_plain_sep_mark()



# --------------------------------------------------------------- #


# Example 9
# 
# Using quatifiers
# 

# Text to match showing
names_to_match ='''        Mr. Schafer
        Mr Smith
        Ms Davis
        Mrs. Robinson
        Mr. T
'''

print("Example 9\nUse quantifiers to limit typing (and potential errors) using {n} - exact quantifier\n\t(n = a number in braces)")

print()

print(f"The names to match:\n{names_to_match}")

print()

pattern_9 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')    

matches_9 = pattern_9.finditer(text_to_search) # assign search result to a var

print("All phone numbers using {n} - exact quantifier (n = a number in braces)")

for match in matches_9:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_9 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')")


output_plain_sep_mark()



# --------------------------------------------------------------- #


# Example 10
# 
# Finding emails
# 

# Text to match showing
emails_to_match ='''        CoreyMSchafer@gmail.com
        corey.schafer@university.edu
        corey-321-schafer@my-work.net
'''

print("Example 10\nUsing regex to find emails")

print(f"\nThe emails to match:\n{emails_to_match}\n")


pattern_10 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')    

matches_10 = pattern_10.finditer(text_to_search) # assign search result to a var

print("All emails from text_to_search")

for match in matches_10:
    print(f'\t{match}')

# print("All words 'Ha' that have a word boundary 'b'")
# count = 1
# for match in matches:
#     if count <= 10:
#         print(f'\t{match}')
#         count += 1

# print('\nCharacters Ha with finds stopped after 10 interations.')

print("\n\tSEARCH PATTERN: pattern_9 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')")


output_plain_sep_mark()
# print("\n\tSEARCH PATTERN: ")

# STOPPED AT 33:57

print()