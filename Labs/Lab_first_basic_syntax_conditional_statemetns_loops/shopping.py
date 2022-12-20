budget = int(input())
product_price = input()
all_product_prices = 0

while product_price != 'End':
    product_price = int(product_price)
    all_product_prices += product_price
    if all_product_prices > budget:
        print(f"You went in overdraft!")
        break

    product_price = input()
else:
    print(f"You bought everything needed.")



