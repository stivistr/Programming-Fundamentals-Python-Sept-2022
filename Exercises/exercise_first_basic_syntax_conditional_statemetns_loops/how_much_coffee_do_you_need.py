command = input()
coffee_needed = 0

while command != "END":
    if command == "dog" or \
            command == "cat" or \
            command == "coding" or \
            command == "movie":
        coffee_needed += 1
    elif command.isupper():
        coffee_needed += 2
    command = input()
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)

