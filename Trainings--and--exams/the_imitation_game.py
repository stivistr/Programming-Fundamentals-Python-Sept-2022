encrypted_message = input()

while True:

    command = input().split('|')

    if command[0] == 'Decode':
        print(f"The decrypted message is: {encrypted_message}")
        break

    current_command = command[0]

    if current_command == "Move":
        number_of_letters = int(command[1])
        first_part = encrypted_message[:number_of_letters]
        encrypted_message = encrypted_message.replace(encrypted_message[:number_of_letters], '')
        encrypted_message = encrypted_message + first_part

    elif current_command == 'Insert':
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif current_command == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

