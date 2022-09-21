import re

text = input()
red = re.findall('([A-Z])', text)
indexes = list(red)

for i in range(len(text)):
    red = re.findall('([A-Z])', text)
    indexes = list(red)

