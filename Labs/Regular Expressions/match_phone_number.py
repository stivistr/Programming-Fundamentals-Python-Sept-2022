import re

data = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
result = re.findall(pattern, data)
print(', '.join(result))