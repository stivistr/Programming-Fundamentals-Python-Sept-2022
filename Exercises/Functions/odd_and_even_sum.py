def odd_and_even_sum(whole_digit):
    odd_sum = 0
    even_sum = 0
    for digit in str(whole_digit):
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return (f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = int(input())
result = odd_and_even_sum(number)
print(odd_and_even_sum(number))