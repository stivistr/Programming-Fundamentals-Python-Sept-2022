list_of_chars = input().split(', ')
ascii_dictionary = {}

for char in list_of_chars:
    if char not in ascii_dictionary:
        ascii_dictionary[char] = ord(char)

print(ascii_dictionary)