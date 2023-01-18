def angry_cat(prices):
    left_side_sum = 0
    right_side_sum = 0
    left_side = prices[0:entry_point]
    right_side = prices[entry_point + 1::]
    for price in range(len(left_side)):
        if type_of_item == 'cheap':
            if left_side[price] < prices[entry_point]:
                left_side_sum += left_side[price]
        elif type_of_item == 'expensive':
            if left_side[price] >= prices[entry_point]:
                left_side_sum += left_side[price]
    for price in range(len(right_side)):
        if type_of_item == 'cheap':
            if right_side[price] < prices[entry_point]:
                right_side_sum += right_side[price]
        elif type_of_item == 'expensive':
            if right_side[price] >= prices[entry_point]:
                right_side_sum += right_side[price]

    if left_side_sum > right_side_sum:
        print(f"Left - {left_side_sum}")
    elif right_side_sum > left_side_sum:
        print(f"Right - {right_side_sum}")
    else:
        print(f"Left - {left_side_sum}")


price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_of_item = input()
angry_cat(price_ratings)
