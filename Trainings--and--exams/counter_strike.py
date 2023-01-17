energy = int(input())
current_distance = input()
won_battles = 0

while True:
    if current_distance == 'End of battle':
        print(f'Won battles: {won_battles}. Energy left: {int(energy)}')
        break
    if energy >= float(current_distance):
        energy -= float(current_distance)
        won_battles += 1
        current_distance = input()
        if won_battles % 3 == 0:
            energy += won_battles
    else:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {int(energy)} energy')
        break

