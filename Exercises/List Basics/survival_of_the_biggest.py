list_of_numbers = list(map(int, input().split()))
numbers_to_remove = int(input())

for number in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

print(', '.join(str(num) for num in list_of_numbers))