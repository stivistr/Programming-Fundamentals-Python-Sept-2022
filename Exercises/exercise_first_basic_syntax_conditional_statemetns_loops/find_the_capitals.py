text = input()

capital_letters = []

for i, v in enumerate(text):
    if v.isupper():
        capital_letters.append(i)

print(capital_letters)

