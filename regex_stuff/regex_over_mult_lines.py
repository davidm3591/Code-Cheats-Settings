import re
# multiple line for long regex

text_string = """
Hello
there
I am
a long
string
used
for
an
example
"""

pattern = re.compile(
    r'Hello|'
    r'there|'
    r'I am|'
    r'a long|'
    r'string')

# pattern = re.compile(r'Hello
#     r'there'
#     r'I am'
#     r'a long'
#     r'string')


matches = pattern.finditer(text_string)

for match in matches:
    print(match)

audio_text = """
hint
entry
hint1
hint2
hint3
hint4
transition
transition1
transition2
exit
"""
audio = re.compile(
    r"(\bentry\b|\bhint\b|\bhint1\b|"
    r"\bhint2\b|\bhint3\b|\bhint4\b|"
    r"\btrans\w+\b|\btrans\w+1\b|\btrans\w+2\b|"
    r"\bexit\b)"
    , re.IGNORECASE
    )
# r"\bexit\b)\sAudio:\s(.+)"

matches_1 = audio.finditer(audio_text)

for match_1 in matches_1:
    print(match_1)
