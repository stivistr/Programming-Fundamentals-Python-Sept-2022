number = int(input())

for i in sorted(str(number), reverse=True):
    print(i, end='')

