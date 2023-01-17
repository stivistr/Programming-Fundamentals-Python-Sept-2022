def swap_func(number1, number2, sequence):
    sequence[number1], sequence[number2] = sequence[number2], sequence[number1]
    return sequence


def multiply_func(number1, number2, sequence):
    sequence[number1] = sequence[number1] * sequence[number2]
    return sequence


def decrease_func(sequence):
    decrease = [num - 1 for num in sequence]
    return decrease


def modified_array(sequence):
    while True:
        command = input()

        if command == 'end':
            break
        elif command == 'decrease':
            sequence = decrease_func(sequence)
            continue

        current_command, index1, index2 = command.split()

        if current_command == 'swap':
            swap_func(int(index1), int(index2), sequence)
        elif current_command == 'multiply':
            multiply_func(int(index1), int(index2), sequence)

    print(', '.join(str(digit) for digit in sequence))


array = list(map(int, input().split()))
modified_array(array)
