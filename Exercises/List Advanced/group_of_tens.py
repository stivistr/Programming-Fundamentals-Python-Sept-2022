sequence_of_numbers = list(map(int, input().split(', ')))

group_of_10 = []
group_of_20 = []
group_of_30 = []
group_of_40 = []
group_of_50 = []


for num in sequence_of_numbers:
    if 0 < num <= 10:
        group_of_10.append(num)
        print(f"Group of {group_of_10}'s: {group_of_10}")