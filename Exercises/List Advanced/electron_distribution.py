number_of_electrons = int(input())

shells = []

for shell in range(1, number_of_electrons + 1):
    box = 2 * (shell ** 2)
    if box > number_of_electrons:
        shells.append(number_of_electrons)
        break
    shells.append(box)
    number_of_electrons -= box
    if number_of_electrons <= 0:
        break

print(shells)
