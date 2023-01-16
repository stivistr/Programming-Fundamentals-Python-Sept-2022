import re

bought_furniture = []
money_spend = 0
command = input()
pattern = r">>([A-Za-z]+)<<(\d+\.*\d+)!(\d{1,})"
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        money_spend += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
if bought_furniture:
    print('\n'.join(bought_furniture))
print(f"Total money spend: {money_spend:.2f}")