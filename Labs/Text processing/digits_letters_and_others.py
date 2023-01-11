sequence_of_chars = input()

digits = []
letters = []
others = []

for char in sequence_of_chars:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        others.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(others))
