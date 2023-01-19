activation_key = input()

while True:

    command = input().split('>>>')

    if command[0] == 'Generate':
        print(f"Your activation key is: {activation_key}")
        break

    current_command = command[0]

    if current_command == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif current_command == 'Flip':
        start_index = int(command[2])
        final_index = int(command[3])
        size = command[1]
        if size == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[start_index:final_index].upper() + \
                             activation_key[final_index:]
            print(activation_key)
        elif size == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:final_index].lower() + \
                             activation_key[final_index:]
            print(activation_key)

    elif current_command == 'Slice':
        start_index = int(command[1])
        final_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[final_index:]
        print(activation_key)
