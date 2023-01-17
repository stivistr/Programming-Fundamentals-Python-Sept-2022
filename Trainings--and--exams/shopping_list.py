def urgent_func(product, items):
    if product in items:
        exit()

    groceries.insert(0, product)
    return items


def unnecessary_func(product, items):
    if product in items:
        groceries.remove(product)

    return items


def correct_func(product1, product2, items):
    if product1 in items:
        items.remove(items[product1])
        items.insert(items[product1], product2)

    return items


def rearrange_func(product, items):
    if product in items:
        items.pop(product)
        items.append(product)

    return items


def groceries_list(products):
    while True:
        command = input()

        if command == 'Go Shopping!':
            break

        command_split = command.split()
        current_command = command_split[0]

        if current_command == 'Urgent':
            item = command[1]
            urgent_func(item, products)
        elif current_command == 'Unnecessary':
            item = command[1]
            unnecessary_func(item, products)
        elif current_command == 'Correct':
            item1 = command[1]
            item2 = command[-1]
            correct_func(item1, item2, products)
        elif current_command == 'Rearrange':
            item = command[1]
            rearrange_func(item, products)

    print(', '.join(products))


groceries = input().split('!')
groceries_list(groceries)
