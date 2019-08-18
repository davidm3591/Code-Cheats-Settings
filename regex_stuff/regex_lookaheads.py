# Python regex Lookarounds

########                    Positive Lookahead    x(?=y)               ########

# in example one, we are looking for a primary match of four digits '\d{4}'
# Our condition, in the form of a lookahead, is that our match is followed by
# space, and then 'Amphitheatre'

########                    Negative Lookahead    x(?!=y)              ########

# in example two, we are looking for a primary match of four digits '\d{4}'
# Our condition this time, again a lookahead, is that our match is NOT
# followed by space, and then 'Amphitheatre'

import re

address = "1600 Amphitheatre Parkway Mountain View, CA 94043"

result_1 = re.findall('\d{4}(?=\sAmphitheatre)', address)

result_2 = re.findall('\d{4}(?!\sAmphitheatre)', address)

print(f"result 1 is: {result_1}")
print("\n")
print(f"result 2 is: {result_2}")
