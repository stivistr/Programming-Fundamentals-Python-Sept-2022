command = input()
dup1 = str()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for char in command:
        dup1 = char + char
        print(dup1, end='')
    print()
    command = input()


