dungeon_rooms = input().split('|')
health = 100
bitcoins = 0

for room in dungeon_rooms:
    current_data, amount = room.split()
    if current_data == 'potion':
        damaged_health = 100 - health
        health += int(amount)
        if int(amount) > damaged_health:
            print(f"You healed for {damaged_health} hp.")
        else:
            print(f"You healed for {amount} hp.")
        if health > 100:
            health = 100
        print(f"Current health: {health} hp.")
    elif current_data == 'chest':
        bitcoins += int(amount)
        print(f"You found {amount} bitcoins.")
    else:
        health -= int(amount)
        if health > 0:
            print(f"You slayed {current_data}.")
        else:
            print(f"You died! Killed by {current_data}.")
            print(f"Best room: {dungeon_rooms.index(room) + 1}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
