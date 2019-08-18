# ################################################################## ###
# ###                                                                ###
# ###   Python Tutorial: re Module - How to Write and Match          ###
# ###   Regular Expressions (Regex)                                  ###
# ###                                                                ###
# ###   Corey Schafer: https://www.youtube.com/watch?v=K8L6KVGG-7o   ###
# ###   Tutorial files (code_snippets/Python-Regular_Expressiosns):  ###
# ###   https://github.com/CoreyMSchafer/                            ###
# ###                                                                ###
# ###   INDEX:                                                       ###
# ###     1. Simple (simple.py)                                      ###
# ###       1.1. Raw strings                                         ###
# ###       1.2. re.compile method                                   ###
# ###       1.3. finditer                                            ###
# ###       1.4. Use index of variable to grab match                 ###
# ###       1.5. Metacharacters (need to be escaped with \)          ###
# ###       1.6. Metacharcters - pattern matching                    ###
# ###           1.6.1. Character classes                             ###
# ###           1.6.2. Anchors                                       ###
# ###           1.6.3. Quantifiers                                   ###
# ###       1.7. Examples (patterns: metacharcters, anchors,         ###
# ###            boundaries)                                         ###
# ###           1.7.1 Phone numbers                                  ###
# ###               - No quatifiers                                  ###
# ###               - Quantifiers                                    ###
# ###                                                                ###
# ###     2. Emails (emails.py)                                      ###
# ###                                                                ###
# ###     3. URLs (urls.py)                                          ###
# ###                                                                ###                                                                ###
# ###                                                                ###
# ################################################################## ###

import re


def ln_brk():
    print('\n')


sep_marker = "\n"
sep_marker += 5 * "-------------"
# ###########################   1. Simple   ############################


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
456_555_1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'


# 1.1 Raw strings - prefaced with an r - tells python not to handle
#     backslashes "\" in any special way
# ----------------------------------------------------------------------
print('\tTab')      # backslash as an escape (tab)
print(r'\tTab')     # Ignore backslash as an escape
# ----------------------------------------------------------------------
ln_brk()


# 1.2 re.compile - allows separating expression out into a variable
# ----------------------------------------------------------------------
pattern = re.compile(r'abc')    # search for literal
# ----------------------------------------------------------------------


# 1.3 .finditer() - iterates thru search content
# ----------------------------------------------------------------------
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ----------------------------------------------------------------------
ln_brk()


# 1.4 Use index of variable to grab match
#     Example return: <re.Match object; span=(1, 4), match='abc'>
# ----------------------------------------------------------------------
print(text_to_search[1:4])
# ----------------------------------------------------------------------
ln_brk()


# 1.5 Metacharacters - need to be escaped with backslash "\"
# ----------------------------------------------------------------------
# Period not escaped
pattern1 = re.compile(r'.')  # period: all characters except new line
matches1 = pattern1.finditer(text_to_search)

for match1 in matches1:
    print(match1)

# Period escaped
pattern2 = re.compile(r'coreyms\.com')
matches2 = pattern2.finditer(text_to_search)

for match2 in matches2:
    print(match2)

backslash = r'''
Regualar Expression Metacharcters: . ^ $ * + ? { } [ ] \ | ( )
'''
print(backslash)
# ----------------------------------------------------------------------
ln_brk()


# 1.6 Metacharacters - pattern matching with metacharacters
# ----------------------------------------------------------------------

# 1.6.1 Character Classes #
# Check for numbers 0-9
print(r"Match all digits 0-9 with \d")
pattern3 = re.compile(r'\d')  # backslash d: digits 0-9
matches3 = pattern3.finditer(text_to_search)

for match3 in matches3:
    print(match3)

# Check for non-digits that are not 0-9
ln_brk()
print(r"Match all non-digits (not 0-9) with \D")
pattern4 = re.compile(r'\D')
matches4 = pattern4.finditer(text_to_search)

for match4 in matches4:
    print(match4)

# Check for word character (a-z, A-Z, 0-9, _)
ln_brk()
print(r"Match all word characters (a-z, A-Z, 0-9, _) with \w")
pattern5 = re.compile(r'\D')
matches5 = pattern5.finditer(text_to_search)

for match5 in matches5:
    print(match5)

# Check for non-word characters - not (a-z, A-Z, 0-9, _)
ln_brk()
print(r"Match all non-word characters (not (a-z, A-Z, 0-9, _)) with \W")
pattern6 = re.compile(r'\W')
matches6 = pattern6.finditer(text_to_search)

for match6 in matches6:
    print(match6)


# 1.6.2 Anchors (position) #
# Check for literal with leading word boundry - \b
ln_brk()
print(r"Match all literal 'Ha' that have a leading word boundary with \b")
pattern7 = re.compile(r'\bHa')
matches7 = pattern7.finditer(text_to_search)

for match7 in matches7:
    print(match7)

# Check for literal with trailing word boundry - \b
ln_brk()
print(r"Match all literal 'Ha' that have a trailing word boundary with \b")
pattern8 = re.compile(r'Ha\b')
matches8 = pattern8.finditer(text_to_search)

for match8 in matches8:
    print(match8)

# Check for literal with leading & trailing word boundry - \b
ln_brk()
print(r"Match all literal 'Ha' that have a leading & trailing word boundary with \b")
pattern9 = re.compile(r'\bHa\b')
matches9 = pattern9.finditer(text_to_search)

for match9 in matches9:
    print(match9)

# Check for literal at beginning of string with ^ (caret)
ln_brk()
print("Check for literal 'Start' at beginning of string with ^ (caret)")
pattern10 = re.compile(r'^Start')
matches10 = pattern10.finditer(sentence)

for match10 in matches10:
    print(match10)


# Check for literal at end of string with $ (dollar)
ln_brk()
print("Check for literal 'end' at end of string with $ (dollar)")
pattern11 = re.compile(r'end$')
matches11 = pattern11.finditer(sentence)

for match11 in matches11:
    print(match11)
# ----------------------------------------------------------------------


# 1.7 Examples patterns: metacharcters, anchors, boundaries
# ----------------------------------------------------------------------

# 1.7.1 Phone numbers #
# Phone numbers with \d and no quantifier
ln_brk()
print(f"Phone numbers with \d and no quantifier{sep_marker}")
# 3 digits, any character, 3 digits, any character, 4 digits
pattern12 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches12 = pattern12.finditer(text_to_search)

for match12 in matches12:
    print(match12)

# Phone numbers with \d and no quantifier from external text file
ln_brk()
print(f"Phone numbers with \d and no quantifier "
      f"from external text file{sep_marker}")

with open('data.txt', 'r') as f:
    contents = f.read()

    pattern13 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches13 = pattern13.finditer(contents)

    for match13 in matches13:
        print(match13)

# Phone numbers with \d, no quantifier, '-' or '.' separator
# with charcter set []
ln_brk()
print(f"Phone numbers with \d, no quantifier, \n'-' or '.' "
      f"separator withcharcter set [-.]{sep_marker}")
pattern14 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches14 = pattern14.finditer(text_to_search)

for match14 in matches14:
    print(match14)

# 800 or 900 phone numbers with [89], no quantifier, '-' or '.' separator
# with []
ln_brk()
print(f"800 or 900 phone numbers with [89], no \nquantifier, '-' or '.' "
      f"separator [-.]{sep_marker}")
pattern15 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches15 = pattern15.finditer(text_to_search)

for match15 in matches15:
    print(match15)

# 800 or 900 phone numbers with [89], no quantifier, '-' or '.' separator
# with [] from external text file
ln_brk()
print(f"800 or 900 phone numbers with [89], no \nquantifier, '-' or '.' "
      f"separator [-.] from external text file{sep_marker}")
pattern16 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

with open('data.txt', 'r') as f:
    contents1 = f.read()
    matches16 = pattern16.finditer(contents1)

    for match16 in matches16:
        print(match16)

# Phone numbers with \d and exact number quantifier { }
ln_brk()
print("Phone numbers with \d and exact number quantifier { }" + sep_marker)
# 3 digits, any character, 3 digits, any character, 4 digits
pattern17 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches17 = pattern17.finditer(text_to_search)

for match17 in matches17:
    print(match17)
# ----------------------------------------------------------------------
# Stopped at 14:00
