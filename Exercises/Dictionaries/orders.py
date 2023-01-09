orders = {}

while True:

    command = input()
    if command == 'buy':
        break

    name, price, quantity = command.split()
    if name not in orders.keys():
        orders[name] = [int(quantity), float(price)]
    else:
        orders[name][0] += int(quantity)
        if orders[name][1] != float(price):
            orders[name][1] = float(price)

for name, value in orders.items():
    print(f"{name} -> {orders[name][0] * orders[name][1]:.2f}")



    