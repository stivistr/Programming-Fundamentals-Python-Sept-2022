def greater_than_average(sequence):
    average = sum(sequence) / len(sequence)
    greaters = [num for num in sequence if num > average]
    greaters.sort(reverse=True)
    if not greaters:
        print('No')
    while len(greaters) > 5:
        greaters.pop(-1)

    print(' '.join(str(digit) for digit in greaters))


sequence_of_integers = list(map(int, input().split()))
greater_than_average(sequence_of_integers)
