def total_price_of_order(product, quantity):
    if product == 'coffee':
        return quantity * 1.50
    elif product == 'coke':
        return quantity * 1.40
    elif product == 'water':
        return quantity * 1.00
    elif product == 'snacks':
        return quantity * 2.00


current_product = input()
quantity_of_the_product = int(input())
total_price = total_price_of_order(current_product, quantity_of_the_product)
print(f'{total_price:.2f}')
