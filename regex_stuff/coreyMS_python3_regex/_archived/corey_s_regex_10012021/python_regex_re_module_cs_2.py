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

cat
rat
mat
sat
bat
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
print("Return phone numbers that use any type of separator")
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)

with open('regex_stuff\coreyMS_python3_regex\data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)
    
    for match in matches:
        print(match)


print() # space
# 
# Matching specific content in brackets as character sets
# 
print("Return only phone numbers that use '.' or '-' separators")
pattern_1 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')   # match ph nums that
                                                        # use a . or - separator
matches_1 = pattern_1.finditer(text_to_search)

with open('regex_stuff\coreyMS_python3_regex\data.txt', 'r') as f:
    contents = f.read()

    for match_1 in matches_1:
        print(match_1)


print() # space
# 
# Matching 800 and 900 in character sets
# 
print("Return 800 and 900 phone numbers that use '.' or '-' separators")
pattern_2 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') # match 800 & 900 nums
                                                        # that use . or - 
                                                        # separator
matches_2 = pattern_2.finditer(text_to_search)

with open('regex_stuff\coreyMS_python3_regex\data.txt', 'r') as f:
    contents = f.read()

    for match_2 in matches_2:
        print(match_2)


# 
# using the "^" within a character set negates the character set
#   re.compile(r'[^a-zA-Z]') will return everything not an upper or
#   lowercase letter
# 
print() # space
print("Return everything not an upper or lowercase letter")
pattern_3 = re.compile(r'[^a-zA-Z]')     # this finds everything except an
                                         # upper or lower case letter
matches_3 = pattern_3.finditer(text_to_search)

for match_3 in matches_3:
    print(match_3)



# 
# using the "^" within a character set negates the character set
#   re.compile(r'[^bB]') will return everything not an upper or
#   lowercase letter
# 
print() # space
print("Return everything not an upper or lowercase letter")
pattern_4 = re.compile(r'[^bB]at')     # this finds everything except an
                                         # upper or lower case letter
matches_4 = pattern_4.finditer(text_to_search)

for match_4 in matches_4:
    print(match_4)




# print() # space
# pattern = re.compile(r'') 
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

