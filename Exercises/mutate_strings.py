first_text = input()
second_text = input()
last_printed = first_text

for ch in range(len(first_text)):
    left_side = second_text[:ch + 1]
    right_side = first_text[ch+1:]
    mutation = left_side + right_side
    if mutation == last_printed:
        continue
    print(mutation)
    last_printed = mutation


