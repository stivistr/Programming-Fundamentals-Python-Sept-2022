sequence_of_numbers = input().split(' ')
numbers_in_list_as_integers = []
for num in sequence_of_numbers:
    numbers_in_list_as_integers.append(int(num))

result = filter(lambda number: number % 2 == 0, numbers_in_list_as_integers)
print(list(result))