text_integers = list(map(int, input().split(', ')))
count_of_beggars = int(input())
final_sum = []
starting_index = 0

while starting_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(starting_index, len(text_integers), count_of_beggars):
        sum_of_current_beggar += text_integers[current_index]

    starting_index += 1
    final_sum.append(sum_of_current_beggar)

print(final_sum)
        



