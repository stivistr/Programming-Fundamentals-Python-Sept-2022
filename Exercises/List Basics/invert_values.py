text = input().split()
opposite_text = []

for symbol in text:
    current_symbol = -int(symbol)
    opposite_text.append(current_symbol)
print(opposite_text)