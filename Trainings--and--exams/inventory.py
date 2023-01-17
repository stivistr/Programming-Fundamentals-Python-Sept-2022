def collect_func(curr_piece, pieces):
    if curr_piece not in pieces:
        pieces.append(curr_piece)

    return pieces


def drop_func(curr_piece, pieces):
    if curr_piece in pieces:
        pieces.remove(curr_piece)

    return pieces


def combine_func(piece1, piece2, pieces):
    if piece1 in pieces:
        piece1_index = pieces.index(piece1)
        pieces.insert(piece1_index + 1, piece2)

    return pieces


def renew_func(curr_piece, pieces):
    if curr_piece in pieces:
        pieces.remove(curr_piece)
        pieces.append(curr_piece)

    return pieces


def journal_sequence(items):
    while True:
        command = input()

        if command == 'Craft!':
            break

        current_command, current_item = command.split(' - ')

        if current_command == 'Collect':
            collect_func(current_item, items)
        elif current_command == 'Drop':
            drop_func(current_item, items)
        elif current_command == 'Combine Items':
            item1, item2 = current_item.split(':')
            combine_func(item1, item2, items)
        elif current_command == 'Renew':
            renew_func(current_item, items)

    print(', '.join(items))


journal = input().split(', ')
journal_sequence(journal)
