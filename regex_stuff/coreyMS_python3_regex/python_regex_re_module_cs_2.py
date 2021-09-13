import re
from typing import Pattern

# 
# Part 2: Practical Applications
# 
# Corey Schafer
# Python Tutorial: re Module - How to Write & Match Regular Expressions (Regex)
# https://www.youtube.com/watch?v=K8L6KVGG-7o
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

sentence = "Start a sentence and then bring it to an end"

# 
# Finding the phone numbers (literal search doesn't work - multiple instances)
# 
# print() # space
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') 
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)



print() # space
# 
# Finding the phone numbers in an external text document
# 
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

with open('regex_stuff\coreyMS_python3_regex\data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)


# 
# Matching specific content in brackets
# 
pattern_1 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')   # match ph nums that
                                                        # use a . or - separator
matches_1 = pattern_1.finditer(text_to_search)

with open('regex_stuff\coreyMS_python3_regex\data.txt', 'r') as f:
    contents = f.read()

    for match in matches_1:
        print(match)


# print() # space
# pattern = re.compile(r'') 
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

