number_of_rooms = int(input())
all_rooms = [input() for room in range(number_of_rooms)]

free_chairs = 0
chairs_needed = 0

for room in all_rooms:
    chairs, visitors = room.split(' ')
    if len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)
    else:
        difference = int(visitors) - len(chairs)
        chairs_needed += difference
        if difference > 0:
            print(f"{difference} more chairs needed in room {all_rooms.index(room) + 1}")

if chairs_needed == 0:
    print(f"Game On, {free_chairs} free chairs left")
