import re


def brk_sep():
    print(6 * '---------')


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
1234-555-900
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)

matches = pattern.search(sentence)

print(matches)

pattern_1 = re.compile(r'\d{3}')
matches_1 = pattern_1.finditer(text_to_search)
# print(matches_1)
for match_1 in matches_1:
    print(match_1)

brk_sep()

pattern_2 = re.compile(r'\b(\d\d\d\d-|\d\d\d-)')
matches_2 = pattern_2.finditer(text_to_search)
# print(matches_2)
for match_2 in matches_2:
    print(match_2)
