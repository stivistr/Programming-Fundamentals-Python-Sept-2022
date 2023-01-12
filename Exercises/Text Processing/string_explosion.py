string_with_explosions = input()
explosion_strenght = 0
string_after_explosions = ''
for char in range(len(string_with_explosions)):
    if explosion_strenght > 0 and string_with_explosions[char] != '>':
        explosion_strenght -= 1
    elif string_with_explosions[char] == '>':
        string_after_explosions += string_with_explosions[char]
        explosion_strenght += int(string_with_explosions[char + 1])
    else:
        string_after_explosions += string_with_explosions[char]
print(string_after_explosions)