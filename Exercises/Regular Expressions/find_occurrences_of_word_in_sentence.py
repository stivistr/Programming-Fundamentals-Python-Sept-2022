import re

sentence = input()
word = input()
pattern = fr"\b{word}+\b"
match = re.findall(pattern, sentence, re.IGNORECASE)
print(len(match))