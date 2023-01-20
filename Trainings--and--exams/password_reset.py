password = input()
new_password = ''
while True:

    command = input().split(' ')

    if command[0] == 'Done':
        print(f"Your password is: {new_password}")
        break

    current_command = command[0]

    if current_command == 'TakeOdd':
        for char in range(len(password)):
            if char % 2 != 0:
                new_password += password[char]
        print(new_password)

    elif current_command == 'Cut':
        index = int(command[1])
        lenght = int(command[2])
        new_password = new_password[:index] + '' + new_password[index + lenght:]
        print(new_password)

    elif current_command == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")