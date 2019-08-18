import re


def ex_heading(ex_name):
    delin = 9 * '--------'
    print(f'\n{ex_name}\n{delin}')


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

print(f'URLs to match:{urls}')

ex_heading('Match urls with "https?://(www\.)?\w+\.\w+"')
pattern_1 = re.compile('https?://(www\.)?\w+\.\w+')
matches_1 = pattern_1.finditer(urls)
for match_1 in matches_1:
    print(match_1)

# @ 43:00
ex_heading(f'"https?://(www\.)?\(w+)(\.\w+)"\nCapture domain '
           f'name and top level domain. Put\ndomain name and '
           f'top level domain name in a group')
pattern_2 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches_2 = pattern_2.finditer(urls)
domain_name = "Domain name: "
top_domain = "Domain top-level: "
count = 0
for match_2 in matches_2:
    # print(match_2)
    # print(match_2.group(0))
    count += 1
    print(f'Count: {count}')
    print(f'\t{domain_name}{match_2.group(2)}')
    print(f'\t{top_domain}{match_2.group(3)}')


ex_heading(f'Using back-refernces as shorthand for the group method\n'
    f'"subbed_urls = pattern.sub(r\'\\2\\3\', urls)"')
subbed_urls = pattern_2.sub(r'\2\3', urls)
print(subbed_urls)
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(3))
