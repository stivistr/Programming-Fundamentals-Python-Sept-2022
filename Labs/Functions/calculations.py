def calculator(operator):
    if operator == 'multiply':
        return first_digit * second_digit
    elif operator == 'divide':
        return first_digit // second_digit
    elif operator == 'add':
        return first_digit + second_digit
    elif operator == 'subtract':
        return first_digit - second_digit


operator_as_string = input()
first_digit = int(input())
second_digit = int(input())
calculator(operator_as_string)
print(calculator(operator_as_string))

