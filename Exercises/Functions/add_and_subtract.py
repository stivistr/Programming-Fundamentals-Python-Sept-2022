def sum_numbers(digit1, digit2):
    return digit1 + digit2


def subtract(sum_numbers, digit3):
    return sum_numbers - digit3


def add_and_subtract(digit1, digit2, digit3):
    sum_of_two = sum_numbers(digit1, digit2)
    final_subtract = subtract(sum_of_two, digit3)
    return final_subtract


first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
result = add_and_subtract(first_digit, second_digit, third_digit)
print(result)
