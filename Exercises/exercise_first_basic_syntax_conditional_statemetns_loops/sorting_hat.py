name = input()

while True:
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    lenght_of_name = len(name)
    if lenght_of_name < 5:
        print(f"{name} goes to Gryffindor.")
    elif lenght_of_name == 5:
        print(f"{name} goes to Slytherin.")
    elif lenght_of_name == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()





