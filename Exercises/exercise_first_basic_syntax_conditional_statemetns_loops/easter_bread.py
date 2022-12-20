budget = float(input())
price_for_flour = float(input())
price_for_eggs = price_for_flour * 0.75
price_for_liter_milk = price_for_flour * 1.25 / 4
price_for_bread = price_for_eggs + price_for_flour + price_for_liter_milk
colored_eggs = 0
bread_count = 0

while budget >= price_for_bread:
    bread_count += 1
    budget -= price_for_bread
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


