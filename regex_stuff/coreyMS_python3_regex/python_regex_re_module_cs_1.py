import re

# 
# Part 1: Introduction
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
# Python raw strings 
# 
# Raw strings are handled such that escape and other standard
#   back slash content are ignored
# 
print() # space
print("\tTab") # enters tab before text
print() # space
print(r"\tTab") # ignores escape backslash
print() # space


# 
# Python re.compile() method 
# 
# Allows use (and reuse) of a variable
# 
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# returns: <re.Match object; span=(1, 4), match='abc'>
# use the return span to locate and print match
print(text_to_search[1:4])


print() # space
pattern = re.compile(r'.') # this will pull everything
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print() # space
pattern = re.compile(r'coreyms\.com') # this will look for a literal period
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print() # space
pattern = re.compile(r'\d') # this will find all digits 0 - 9
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print() # space
pattern = re.compile(r'\D') # this will find everything but digits 0 - 9
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# 
# using lowercase "w" is common - returns a-z, A-Z, 0-9, and _
# 
print() # space
pattern = re.compile(r'\w') # this will find 'word' characters
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print() # space
pattern = re.compile(r'\W') # this will find 'non-word' characters
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# 
# using lowercase "B" returns search criteria NOT preceeded by
#   a word boundry (space or non alpha-numeric character)
# 
print() # space
pattern = re.compile(r'\BHa')   # this finds letters H and a that
                                # are not preceded by a space
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# 
# using the "^" and "$" returns search criteria that is at the
#   beginning or end of a string
# Note: the "^" preceeds the search criteria and the "$" follows it
# 
# Ref from top of file: sentence = "Start a sentence and 
# then bring it to an end"
# 
print() # space
pattern = re.compile(r'^Start')     # this finds the word "Start" if it
                                    # is at the beginning of a string
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

print() # space
pattern = re.compile(r'end$')     # this finds the word "end" if it
                                    # is at the end of a string
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
