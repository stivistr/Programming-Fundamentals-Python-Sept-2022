def characters_in_range(char1, char2):
    chars_in_list = []
    for char in range(ord(char1) + 1, ord(char2)):
        chars_in_list.append(chr(char))
    return chars_in_list


character_one = input()
character_two = input()
result = characters_in_range(character_one, character_two)
print(' '.join(result))