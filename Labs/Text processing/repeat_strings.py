sequence_of_strings = input().split()

for word in sequence_of_strings:
    print(word * len(word), end='')