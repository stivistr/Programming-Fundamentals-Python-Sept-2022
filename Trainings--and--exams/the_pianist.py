def store_data_func(number):
    data = {}
    for _ in range(number):
        current_data = input().split('|')
        piece = current_data[0]
        composer = current_data[1]
        key = current_data[2]

        data[piece] = [composer, key]

    return data


def add_func(piece, composer, key, data):
    if piece in data:
        print(f"{piece} is already in the collection!")
    else:
        data[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_func(piece, data):
    if piece in data:
        del data[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key_func(piece, new_key, data):
    if piece in data:
        data[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_func(data):
    result = ''
    for piece in data:
        composer = data[piece][0]
        key = data[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"

    return result


def pianist_func(number):
    data = store_data_func(number)

    while True:

        command = input().split('|')
        if command[0] == 'Stop':
            print(print_func(data))
            break

        current_command = command[0]
        piece = command[1]

        if current_command[0] == 'Add':
            composer = command[2]
            key = command[3]
            add_func(piece, composer, key, data)

        elif current_command[0] == 'Remove':
            remove_func(piece, data)

        elif current_command[0] == 'ChangeKey':
            new_key = command[2]
            change_key_func(piece, new_key, data)


number_of_pieces = int(input())
pianist_func(number_of_pieces)
