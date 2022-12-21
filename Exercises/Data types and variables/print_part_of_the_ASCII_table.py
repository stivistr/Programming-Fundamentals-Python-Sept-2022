first_char_index = int(input())
second_char_index = int(input())

for index in range(first_char_index, second_char_index + 1):
    print(chr(index), end=' ')
