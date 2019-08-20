# python strip method
import re

my_str = "0000000this is string example....wow!!!0000000";

pattern = re.compile(r'0')
# matches = pattern.finditer(my_str)
# matches = pattern.findall(my_str)
matches = pattern.match(my_str)

print(matches)
# print(matches.strip(0))
# count = 0
# for match in matches:
#     count += 1
#     print(f"{count}: {match}")

print(my_str.strip('0'))
