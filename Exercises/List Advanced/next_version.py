number_sequence = list(map(int, input().split('.')))

number_sequence[-1] += 1
if number_sequence[-1] > 9:
    number_sequence [-1] = 0
    number_sequence [1] += 1
    if number_sequence[1] > 9:
        number_sequence[1] = 0
        number_sequence[0] += 1

print('.'.join(str(number) for number in number_sequence))