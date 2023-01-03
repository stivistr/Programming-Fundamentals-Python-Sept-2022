def positive_numbers(numbers):
    positive_digits = [num for num in numbers if num >= 0]
    return ', '.join(str(number) for number in positive_digits)


def negative_numbers(numbers):
    negative_digits = [num for num in numbers if num < 0]
    return ', '.join(str(number) for number in negative_digits)


def even_numbers(numbers):
    even_digits = [num for num in numbers if num % 2 == 0]
    return ', '.join(str(number) for number in even_digits)


def odd_numbers(numbers):
    odd_digits = [num for num in numbers if num % 2 != 0]
    return ', '.join(str(number) for number in odd_digits)


number_sequence = [int(number) for number in input().split(', ')]

print(f'Positive: {positive_numbers(number_sequence)}')
print(f'Negative: {negative_numbers(number_sequence)}')
print(f'Even: {even_numbers(number_sequence)}')
print(f'Odd: {odd_numbers(number_sequence)}')
