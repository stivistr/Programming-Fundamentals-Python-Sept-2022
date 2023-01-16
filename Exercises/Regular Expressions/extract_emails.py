import re

sentence = input()
pattern = r"\s([a-z0-9]+[\.\-\_]*[a-z0-9]+\b@[a-z\-*]+\.[a-z]+\.*[a-z]+)\b"
result = re.findall(pattern, sentence)
print('\n'.join(result))