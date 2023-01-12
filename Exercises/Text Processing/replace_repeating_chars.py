sequence_of_letters = input()
single_letters = ''
for letter in range(len(sequence_of_letters)):
    if letter == len(sequence_of_letters) - 1:
        single_letters += sequence_of_letters[letter]
    elif sequence_of_letters[letter] != sequence_of_letters[letter + 1]:
        single_letters += sequence_of_letters[letter]

print(single_letters)