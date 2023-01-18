vehicles = input().split('>>')

total_tax_collected = 0

for car in vehicles:
    current_car, years, km = car.split()
    if current_car == 'family':
        tax_per_km = int(km) // 3000
        tax_per_year = int(years) * 5
        current_tax_per_car = tax_per_km * 12 + (50 - tax_per_year)
        total_tax_collected += current_tax_per_car
        print(f"A {current_car} car will pay {current_tax_per_car:.2f} euros in taxes.")
    elif current_car == 'heavyDuty':
        tax_per_km = int(km) // 9000
        tax_per_year = int(years) * 8
        current_tax_per_car = tax_per_km * 14 + (80 - tax_per_year)
        total_tax_collected += current_tax_per_car
        print(f"A {current_car} car will pay {current_tax_per_car:.2f} euros in taxes.")
    elif current_car == 'sports':
        tax_per_km = int(km) // 2000
        tax_per_year = int(years) * 9
        current_tax_per_car = tax_per_km * 18 + (100 - tax_per_year)
        total_tax_collected += current_tax_per_car
        print(f"A {current_car} car will pay {current_tax_per_car:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")