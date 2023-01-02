cards = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    first_part = cards[0:middle_of_the_deck]
    second_part = cards[middle_of_the_deck::]
    for card_index in range(len(first_part)):
        final_deck.append(first_part[card_index])
        final_deck.append(second_part[card_index])
    cards = final_deck

print(cards)