food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pig_kilograms = float(input())
days = 30


for current_day in range(1, days + 1):
    food_quantity -= 0.3
    if current_day % 2 == 0:
        hay_quantity -= food_quantity * 0.05
    if current_day % 3 == 0:
        cover_quantity -= pig_kilograms / 3

if food_quantity < 0.3 or hay_quantity < food_quantity * 0.05 or cover_quantity < pig_kilograms / 3:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")

