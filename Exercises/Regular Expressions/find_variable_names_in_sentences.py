import re

sentence = input()
pattern = r"\b_([A-Za-z]+)\b"
result = re.findall(pattern, sentence)
print(','.join(result))