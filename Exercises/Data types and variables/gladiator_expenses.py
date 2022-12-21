lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmets_broken = lost_fights_count // 2
swords_broken = lost_fights_count // 3
shields_broken = lost_fights_count // 6
armors_broken = shields_broken // 2

gladiator_expenses = helmets_broken * helmet_price + swords_broken * sword_price + \
    shields_broken * shield_price + armors_broken * armor_price
print(f'Gladiator expenses: {gladiator_expenses:.2f} aureus')