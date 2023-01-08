elements = input().split()
bakery = {}

for item in range(0, len(elements), 2):
    bakery[elements[item]] = int(elements[item + 1])

print(bakery)