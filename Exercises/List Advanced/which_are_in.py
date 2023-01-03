first_sequence = input().split(', ')
second_sequence = input().split(', ')
which_are_in = [string for string in first_sequence if string in str(second_sequence)]
print(which_are_in)