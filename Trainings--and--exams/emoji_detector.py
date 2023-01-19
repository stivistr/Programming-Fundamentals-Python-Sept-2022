import re

data = input()
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
result = re.findall(pattern, data)
emojis = []
for emoji in result:
    emojis.append(emoji)

cool_threshold = 1

for digit in range(len(data)):
    if data[digit].isdigit():
        cool_threshold *= int(data[digit])

cool_emojis = []


for emj in emojis:
    coolness = 0
    for cool in range(len(emj[1])):
        coolness += ord(emj[1][cool])
    if coolness >= cool_threshold:
        cool_emojis.append(emj)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
cool_emj = ''
for emj in cool_emojis:
    cool_emj += f"{emj[0]}{emj[1]}{emj[0]}\n"
print(cool_emj)