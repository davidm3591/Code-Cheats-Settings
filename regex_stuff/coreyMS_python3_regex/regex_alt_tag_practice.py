import re # standard Python regular expression module
from common_code_snips import *

alt_tags_to_test ='''Image1-alt: Reflection across the y-axis.
Image2-alt: Reflection across the x-axis.
Image3-alt: Reflection across the line y=x.
Image4-alt: This alt text has "quoted" content using double quotes.
Image5-alt: This alt text has 'quoated' content' content using single quotes.
Image6-alt: Using some 1, 2, 3, 4... numbers and ellipsis to boot.
Image7-alt: Let's try an_underscore - not sure why they would want it, but... .
Image8-alt: Might as well throw in a vertical pipe | for grins.
'''
# Working for all tags
alt_tag_pattern_4 = re.compile(r'Image\d-alt:\s*[a-zA-Z0-9\."\',_\|=\s-]+\.')
alt_tag_matches4 = alt_tag_pattern_4.findall(alt_tags_to_test)

print()

for alt_tag_match4 in alt_tag_matches4:
    print(alt_tag_match4)

# this works fine
# alt_tag_pattern1 = re.compile(r'Image\d-alt:')
# alt_tag_matches1 = alt_tag_pattern1.findall(alt_tags_to_test)

# this works
# alt_tag_pattern_2 = re.compile(r'Image\d-alt:\s*[a-zA-Z0-9]+')
# alt_tag_matches2 = alt_tag_pattern2.findall(alt_tags_to_test)
# for alt_tag_match2 in alt_tag_matches2:
#     print(alt_tag_match2)

# this works
# alt_tag_pattern_2_1 = re.compile(r'Image\d-alt:\s*[a-zA-Z0-9=\s-]+\.')
# alt_tag_matches2_1 = alt_tag_pattern2_1.findall(alt_tags_to_test)
# for alt_tag_match2_1 in alt_tag_matches2_1:
#     print(alt_tag_match2_1)

# this works
# alt_tag_pattern_3 = re.compile(r'Image\d-alt:\s*[a-zA-Z0-9\."\',_\|=\s-]+\.')
# alt_tag_matches3 = alt_tag_pattern3.findall(alt_tags_to_test)
# for alt_tag_match3 in alt_tag_matches3:
#     print(alt_tag_match3)

# \s(.+)
print()

# output_plain_sep_title('Regex Worksheet for Alt Tag Project')

print()

# for alt_tag_match1 in alt_tag_matches1:
#     print(alt_tag_match1)


# for x in alt_tags_to_test:
#     print(x)