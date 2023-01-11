word_for_removal = input()
sequence_of_chars = input()

while word_for_removal in sequence_of_chars:
    sequence_of_chars = sequence_of_chars.replace(word_for_removal, '')

print(sequence_of_chars)