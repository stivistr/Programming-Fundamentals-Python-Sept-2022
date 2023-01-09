word_sequence = input().split()
count_characters = {}

for word in word_sequence:
    for char in word:
        if char not in count_characters.keys():
            count_characters[char] = 0
        count_characters[char] += 1

for counter in count_characters.keys():
    print(f"{counter} -> {count_characters[counter]}")