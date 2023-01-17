def cupid_position(numbers):
    while True:
        command = input()

        if command == 'Love!':
            break

        current_command, index = command.split()
        starting_index = 0
        floating_index = 0
        current_index = int(index) + floating_index

        if current_command == 'Jump':
            if int(index) > len(numbers):
                numbers[starting_index] -= 2
            for house in range(numbers[0], len(numbers), int(index)):
                if numbers[house] == 0:
                    print(f"Place {house} already had Valentine's day.")
                numbers[house] -= 2
                if numbers[house] == 0:
                    print(f"Place {house} has Valentine's day.")
                if numbers[house] == numbers[-1]:
                    floating_index += house



stringers_sequence = list(map(int, input().split('@')))
cupid_position(stringers_sequence)
