characters = int(input())
sum_of_characters = 0

for character in range(1, characters + 1):
    current_char = input()
    sum_of_characters += ord(current_char)

print(f'The sum equals: {sum_of_characters}')