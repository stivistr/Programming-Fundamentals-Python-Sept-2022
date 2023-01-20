def plunder_func(town, people, gold, cities):
    if town in cities:
        cities[town][0] -= people
        cities[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    return cities


def prosper_func(town, gold, cities):
    if town in cities:
        if gold < 0:
            print("Gold added cannot be a negative number!")
            return
        else:
            cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")


cities = {}

while True:

    information = input().split('||')

    if information[0] == 'Sail':
        break

    city, population, gold = information[0], int(information[1]), int(information[2])

    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:

    command = input().split('=>')

    if command[0] == 'End':
        if cities:
            town_for_plunder = ''
            print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
            for city in cities:
                town_for_plunder += f"{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg\n"
            print(town_for_plunder)
        break

    current_command = command[0]
    town = command[1]

    if current_command == 'Plunder':
        people = int(command[2])
        gold = int(command[3])
        plunder_func(town, people, gold, cities)

    elif current_command == 'Prosper':
        gold = int(command[2])
        prosper_func(town, gold, cities)
