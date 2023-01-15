import re

data = input()
pattern = r"(\b\d{2})([\/.-])([A-Z][a-z]+)\2(\d{4}\b)"
result = re.findall(pattern, data)
for data in result:
    print(f"Day: {data[0]}, Month: {data[2]}, Year: {data[3]}")