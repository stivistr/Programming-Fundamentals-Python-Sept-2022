import re

data = input()
pattern = r"(\||#)([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
result = re.findall(pattern, data)
calories = 0
for cal in result:
    calories += int(cal[3])

food_for_days = int(calories / 2000)

print(f"You have food to last you for: {food_for_days} days!")

for item in result:
    print(''.join(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}"))