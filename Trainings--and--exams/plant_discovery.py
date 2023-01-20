def store_of_plants(number, store):
    for n in range(number):
        flower = input().split('<->')
        plant = flower[0]
        rarity = int(flower[1])
        store[plant] = [rarity], ''


def add_rating_func(plant, rating, store):
    if plant in store:
        store[plant][1] += rating
    else:
        print('error')


def update_func(plant, new_rarity, store):
    if plant in store:
        store[plant][0] = new_rarity
    else:
        print('error')


def remove_func(plant, store):
    if plant in store:
        store[plant][1] = 0
    else:
        print('error')


def plant_discovery(number):
    store = {}

    store_of_plants(number, store)

    while True:

        command = input().split(': ')

        if command[0] == 'Exhibition':
            print("Plants for the exhibition:")
            for plant in store:
                print(f"- {plant}; Rarity: {store[plant][0]}; Rating: {sum(store[plant][1]) / len(store[plant][1]):.2f}")
            break

        current_command = command[0]
        splitted_command = command[1].split(' - ')

        if current_command == 'Rate':
            plant = splitted_command[0]
            rating = splitted_command[1]
            add_rating_func(plant, rating, store)

        elif current_command == 'Update':
            plant = splitted_command[0]
            new_rarity = int(splitted_command[1])
            update_func(plant, new_rarity, store)

        elif current_command == 'Reset':
            plant = splitted_command[0]
            remove_func(plant, store)


number = int(input())
plant_discovery(number)
