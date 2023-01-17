part_price = input()
price_without_taxes = 0
taxes = 0
total_price = 0

while True:
    if part_price == 'regular':
        break
    if part_price == 'special':
        total_price -= total_price * 0.1
        break
    if float(part_price) > 0:
        price_without_taxes += float(part_price)
        taxes += float(part_price) * 0.2
        part_price = input()
    else:
        print('Invalid price!')
        part_price = input()
        continue
    total_price = price_without_taxes + taxes

if total_price == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total_price:.2f}$')

