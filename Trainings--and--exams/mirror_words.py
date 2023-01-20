import re

data = input()
pattern = r"(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
result = re.findall(pattern, data)
word_pairs = []
counter = 0

for pair in result:
    if pair[1] == pair[3][::-1]:
        word_pairs.append(f'{pair[1]} <=> {pair[3]}')

    counter += 1

if counter > 0:
    print(f"{counter} word pairs found!")

    if not word_pairs:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(', '.join(word_pairs))
else:
    print("No word pairs found!")
    print("No mirror words!")