stops = input()

while True:

    command = input().split(':')

    if command[0] == 'Travel':
        print(f"Ready for world tour! Planned stops: {stops}")
        break

    current_command = command[0]

    if current_command == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif current_command == 'Remove Stop':
        start_index = int(command[1])
        final_index = int(command[2])
        if 0 <= start_index <= final_index < len(stops):
            stops = stops[:start_index] + stops[final_index + 1:]

    elif current_command == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

