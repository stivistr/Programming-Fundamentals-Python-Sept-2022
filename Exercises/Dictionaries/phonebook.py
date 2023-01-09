phonebook = {}

while True:
    command = input()

    if '-' not in command:
        break

    name, number = command.split('-')
    phonebook[name] = number

for income in range(int(command)):
    person = input()
    if person in phonebook.keys():
        print(f"{person} -> {phonebook[person]}")
    else:
        print(f"Contact {person} does not exist.")
