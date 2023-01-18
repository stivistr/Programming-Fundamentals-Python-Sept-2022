data = input()

while True:

    command = input().split()

    if command[0] == 'End':
        break

    current_command = command[0]

    if current_command == 'Translate':
        char = command[1]
        replacement = command[2]
        if char in data:
            data = data.replace(char, replacement)
            print(data)
        else:
            print(data)

    elif current_command == 'Includes':
        substring = command[1]
        if substring in data:
            print('True')
        else:
            print('False')

    elif current_command == 'Start':
        substring = command[1]
        if data.startswith(substring):
            print('True')
        else:
            print('False')

    elif current_command == 'Lowercase':
        data = data.lower()
        print(data)

    elif current_command == 'FindIndex':
        char = command[1]
        last_char = data.rfind(char)
        print(last_char)

    elif current_command == 'Remove':
        start_index = int(command[1])
        count = int(command[2])
        if start_index == 0:
            string_to_remove = data[start_index:count]
            data = data[:start_index] + '' + data[count:]
        else:
            string_to_remove = data[start_index:count + start_index]
            data = data.replace(string_to_remove, '')
        print(data)
