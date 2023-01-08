items = input().split()
searched_products = input().split()
stock = {}

for item in range(0, len(items), 2):
    stock[items[item]] = int(items[item + 1])

for product in searched_products:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")