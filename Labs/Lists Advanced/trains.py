number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command = input()

    if command == 'End':
        break

    current_command = command.split(' ')
    if current_command[0] == 'add':
        number_of_people = int(current_command[1])
        wagons[-1] += number_of_people
    elif current_command[0] == 'insert':
        index = int(current_command[1])
        number_of_people = int(current_command[2])
        wagons[index] += number_of_people
    elif current_command[0] == 'leave':
        index = int(current_command[1])
        number_of_people = int(current_command[2])
        wagons[index] -= number_of_people

print(wagons)