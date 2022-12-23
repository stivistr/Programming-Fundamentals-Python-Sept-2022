factor = int(input())
counter = int(input())
multiples_list = []

for number in range(1, counter + 1):
    current_number = number * factor
    multiples_list.append(current_number)
print(multiples_list)
