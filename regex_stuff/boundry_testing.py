import re

test_text = """
123
321123
abc123
-123
"""

pattern = re.compile(r'\b123\b')

matches = pattern.findall(test_text)
print(matches)
