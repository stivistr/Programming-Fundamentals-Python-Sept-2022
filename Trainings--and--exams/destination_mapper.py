import re

data = input()
pattern = r"(=|\/)[A-Z][A-Za-z]{2,}\1"
result = re.finditer(pattern, data)
points = 0
destinations = []

for destination in result:
    current_destination = re.split('=|\/', destination.group())
    points += len(current_destination[1])
    destinations.append(current_destination[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")