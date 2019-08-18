import re

# ##################### Tutorial Practice Content #####################
# https://github.com/CoreyMSchafer/code_snippets/blob/master/
# Python-Regular-Expressions/simple.py
#
# 1. Literal Searches
#       Text only
#       Text with escaped metacharacter
# 2. Pattern Searches
#


def ex_heading(ex_name):
    delin = 9 * '--------'
    print(f'\n{ex_name}\n{delin}')


# Sample content for search
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

cat
mat
pat
bat
rat
'''

# Sample content for search
sentence = 'Start a sentence and then bring it to an end'


# 1. Search for literals (literal string)
#
# For the most part, regex is not very efficient at searching
# string literals because you are using the Regular Expression engine
# to do the searching. if statement is more efficent
ex_heading('Literal match "abc"')
pattern_1 = re.compile(r'abc')
matches_1 = pattern_1.finditer(text_to_search)
for match_1 in matches_1:
    print(match_1)
print(text_to_search[1:4])  # Use string slicing to print match

ex_heading('Literal match "coreyms.com"')
pattern_2 = re.compile(r'coreyms\.com')  # literal with escaped "."
matches_2 = pattern_2.finditer(text_to_search)
for match_2 in matches_2:
    print(match_2)
print(text_to_search[139:150])  # Use string slicing to print match
# ######################################################################

# 2. Pattern searches
# Pattern searches are what regex is built for

ex_heading('Pattern match for nums: "\d\d\d"')
pattern_3 = re.compile(r'\d\d\d')  # Find all instances of 3 numbers in a row
matches_3 = pattern_3.finditer(text_to_search)
count = 0
for match_3 in matches_3:
    count += 1
    print(f'{count}: {match_3}')

print()

ex_heading('Pattern match for ph #: "\d\d\d.\d\d\d.\d\d\d\d"')
pattern_4 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # basic ph num search
matches_4 = pattern_4.finditer(text_to_search)
count = 0
for match_4 in matches_4:
    count += 1
    print(f'{count}: {match_4}')

print()

ex_heading('Pattern match for nums in txt file: "\d\d\d.\d\d\d.\d\d\d\d"')
pattern_5 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # basic ph num search
with open('data.txt', 'r') as f:
    contents = f.read()

    matches_5 = pattern_5.finditer(contents)  # look for ph # in txt file

    count = 0
    for match_5 in matches_5:
        count += 1
        print(f'{count}: {match_5}')


ex_heading(
    'Pattern match ph # with character set: "\d\d\d[-.]\d\d\d[-.]\d\d\d\d"')
pattern_6 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches_6 = pattern_6.finditer(text_to_search)
count = 0
for match_6 in matches_6:
    count += 1
    print(f'{count}: {match_6}')


ex_heading(
    'Pattern match ph # with character set: "[89]00[-.]\d\d\d[-.]\d\d\d\d"')
pattern_7 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches_7 = pattern_7.finditer(text_to_search)
count = 0
for match_7 in matches_7:
    count += 1
    print(f'{count}: {match_7}')


ex_heading('Match nums in a range"[1-5]"')
pattern_8 = re.compile(r'[1-5]')
matches_8 = pattern_8.finditer(text_to_search)
count = 0
for match_8 in matches_8:
    count += 1
    print(f'{count}: {match_8}')


ex_heading(f'Pattern match for 800 and 900 ph#s in txt '
           f'file: "[89]00[-.]\d\d\d[-.]\d\d\d\d"')
pattern_9 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
with open('data.txt', 'r') as f:
    contents = f.read()
    matches_9 = pattern_9.finditer(contents)  # look for ph # in txt file
    count = 0
    for match_9 in matches_9:
        count += 1
        print(f'{count}: {match_9}')


ex_heading('Match lower and upper case letters in a range"[a-zA-Z]"')
pattern_10 = re.compile(r'[a-zA-Z]')
matches_10 = pattern_10.finditer(text_to_search)
count = 0
for match_10 in matches_10:
    count += 1
    print(f'{count}: {match_10}')


ex_heading('Match characters that are not lower or upper case '
           f'\nletters in a range"[^a-zA-Z]" using the "^" to negate range.')
pattern_11 = re.compile(r'[^a-zA-Z]')
matches_11 = pattern_11.finditer(text_to_search)
count = 0
for match_11 in matches_11:
    count += 1
    print(f'{count}: {match_11}')


ex_heading(f'Match everything with "at" except '
           f'"bat""[^b]at" using "^" as negation symbol')
pattern_12 = re.compile(r'[^b]at')
matches_12 = pattern_12.finditer(text_to_search)
count = 0
for match_12 in matches_12:
    count += 1
    print(f'{count}: {match_12}')


ex_heading('Use "quantifier" for multple characters "\d{3}.\d{3}.\d{4}"')
pattern_13 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches_13 = pattern_13.finditer(text_to_search)
count = 0
for match_13 in matches_13:
    count += 1
    print(f'{count}: {match_13}')


ex_heading(f'Use "quantifier" for an unknown number '
           f'of characters "Mr\.?\s[A-Z]\w*"')
# Qunatifier for unknown number of characters
# ? = 0 or 1 --- \s = white space --- \w word character
# * = 0 or more
pattern_14 = re.compile(r'Mr\.?\s[A-Z]\w*')
matches_14 = pattern_14.finditer(text_to_search)
count = 0
for match_14 in matches_14:
    count += 1
    print(f'{count}: {match_14}')


ex_heading(f'Use "quantifier" for an unknown number '
           f'of characters "M(r|s|rs)\.?\s[A-Z]\w*"')
# Qunatifier for unknown number of characters
# ? = 0 or 1 --- \s = white space --- \w word character
# * = 0 or more and grouping M(r|s|rs)
pattern_15 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches_15 = pattern_15.finditer(text_to_search)
count = 0
for match_15 in matches_15:
    count += 1
    print(f'{count}: {match_15}')


# ex_heading('Match lower and upper case letters in a range"[a-zA-Z]"')

# Find all lower and upper case letters in the range a-z and A-Z
# pattern_10 = re.compile(r'[a-zA-Z]')
# matches_10 = pattern_10.finditer(text_to_search)

# count = 0
# for match_10 in matches_10:
#     count += 1
#     print(f'{count}: {match_10}')

# pattern = re.compile(r'start', re.I)  # literal 'start', re.I ingnore case

# matches = pattern.search(sentence)

# print(matches_2)
# Stopped at:  4/24/2019  18:20
