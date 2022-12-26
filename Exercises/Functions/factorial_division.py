def factorial(digit1, digit2):
    fact_digit1 = 1
    fact_digit2 = 1
    for digit in range(1, digit1 + 1):
        fact_digit1 *= digit
    for num in range(1, digit2 + 1):
        fact_digit2 *= num

    division = fact_digit1 // fact_digit2
    return division


number_one = int(input())
number_two = int(input())
print(f'{factorial(number_one, number_two):.2f}')
