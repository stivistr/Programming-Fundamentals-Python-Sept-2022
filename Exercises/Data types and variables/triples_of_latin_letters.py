number = int(input())

for first_character in range(number):
    for second_character in range(number):
        for third_character in range(number):
            print(f"{chr(97 + first_character)}{chr(97 + second_character)}{chr(97 + third_character)}")
