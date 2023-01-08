stock = {}

while True:
    command = input()

    if command == 'statistics':
        break

    key, value = command.split(': ')
    if key not in stock:
        stock[key] = int(value)
    else:
        stock[key] += int(value)

print("Products in stock:")
for product in stock:
    print(f"- {product}: {stock[product]}")
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")