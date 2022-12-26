numbers = input().split(' ')
numbers_in_list = []
for num in numbers:
    numbers_in_list.append(int(num))

print(f"The minimum number is {min(numbers_in_list)}")
print(f"The maximum number is {max(numbers_in_list)}")
print(f"The sum number is: {sum(numbers_in_list)}")