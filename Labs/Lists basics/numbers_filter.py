number_of_lines = int(input())

command_even = 'even'
command_odd = 'odd'
command_positive = 'positive'
command_negative = 'negative'

list_of_numbers = []

for num in range(number_of_lines):
    current_number = int(input())
    list_of_numbers.append(current_number)

command_list = []
command = input()

for number in list_of_numbers:
    if (
            (command == command_even and number % 2 == 0) or
            (command == command_odd and number % 2 != 0) or
            (command == command_negative and number < 0) or
            (command == command_positive and number >= 0)
    ):
        command_list.append(number)

print(command_list)