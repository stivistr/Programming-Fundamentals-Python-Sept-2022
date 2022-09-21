n = int(input())

for num in range(0, n):
    current_num = int(input())
    if current_num % 2 != 0:
        print(f'{current_num} is odd!')
        break
else:
    print(f'All numbers are even.')