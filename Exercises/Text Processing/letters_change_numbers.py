hidden_number = input().split()
result = 0
for number in hidden_number:
    current_number = int(number[1:len(number) - 1])
    first_letter = number[0]
    last_letter = number[-1]
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        result += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        result += current_number * first_letter_position
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        result -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        result += last_letter_position
print(f'{result:.2f}')
