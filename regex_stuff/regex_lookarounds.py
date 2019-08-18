import re
####################### Python REGEX Lookarounds #######################


########        Definitions, Regular Expressions (regex)        ########

# Capture v. Consume
# 1. Capture groups and non-capture groups
#    1.1. Non-capture groups will make a match, but will not return it
#    1.2. Capture groups collect and return the match

# 2. Lookahead and Lookbehind, Zero-Length Assertions
#    Lookahead and lookbehind, collectively called "lookaround",
#    are zero-length assertions that start and end at word anchors.
#    A lookaround actually matches characters, but then gives up
#    the match, returning only the result: match or no match.
#    That is why they are called "assertions". They do not consume
#    characters in the string, but only assert whether a match is
#    possible or not.

# 3. There Are Four Types of Lookarounds
#    3.1. Positive Lookahead ?=
#    3.2. Negative Lookahead ?!
#    3.3. Positive Lookbehind ?<=
#    3.4. Negative Lookbehind ?<!


# text_to_match = "The sentence."
# text_to_match = "1001.1"
# text_to_match = "1234-56-78"
# text_to_match = "\\1234-56-78."
# text_to_match = "\\12345-67-89."
# text_to_match = "12345-67-89"
text_to_match = "123456-78-99"
# text_to_match = "."

test_1 = re.compile('\b\w+\b')
matches_1 = test_1.finditer(text_to_match)
for match in matches_1:
    print(f'test_1 match: {match}')

test_2 = re.compile('\b\w+\w')
matches_2 = test_2.finditer(text_to_match)
for match in matches_2:
    print(f'test_2 match: {match}')

test_3 = re.compile('\w+\w')
matches_3 = test_3.finditer(text_to_match)
for match in matches_3:
    print(f'test_3 match: {match}')

test_4 = re.compile('\w+\b')
matches_4 = test_4.finditer(text_to_match)
for match in matches_4:
    print(f'test_4 match: {match}')

test_1A = re.compile('\b\w+\b')
matches_1A = test_1A.findall(text_to_match)
print(f'test_1A matches_1A: {matches_1A}')

test_2A = re.compile('\b\w+\w')
matches_2A = test_2A.findall(text_to_match)
print(f'test_2A matches_2A: {matches_2A}')

test_3A = re.compile('\w+\w')
matches_3A = test_3A.findall(text_to_match)
print(f'test_3A matches_3A: {matches_3A}')

test_4A = re.compile('\w+\b')
matches_4A = test_4A.findall(text_to_match)
print(f'test_4A matches_4A: {matches_4A}')

test_5A = re.compile('\b')
matches_5A = test_5A.findall(text_to_match)
print(f'test_5A matches_5A: {matches_5A}')

test_6A = re.compile('\W')
matches_6A = test_6A.findall(text_to_match)
print(f'test_6A matches_6A: {matches_6A}')

test_7A = re.compile('\B')
matches_7A = test_7A.findall(text_to_match)
print(f'test_7A matches_7A: {matches_7A}')

test_8A = re.compile('\d{4,5}-\d{2}-\d{2}')
matches_8A = test_8A.findall(text_to_match)
print(f'test_8A matches_8A: {matches_8A}')

test_9A = re.compile('[\d{4}|\d{5}]-\d{2}-\d{2}')
matches_9A = test_9A.findall(text_to_match)
print(f'test_9A matches_9A: {matches_9A}')

test_10A = re.compile('(?=\b)\d{4,5}-\d{2}-\d{2}')
matches_10A = test_10A.findall(text_to_match)
print(f'test_10A matches_10A: {matches_10A}')
