def garage_func(num, garage):
    for n in range(num):
        car, mileage, fuel = input().split('|')
        garage[car] = [int(mileage), int(fuel)]

    return garage


def drive_func(current_car, distance, current_fuel, garage):

    if current_car in garage:
        if garage[current_car][1] >= current_fuel:
            if garage[current_car][0] + distance >= 100000:
                print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
                print(f"Time to sell the {current_car}!")
                del garage[current_car]
            else:
                garage[current_car][0] += distance
                garage[current_car][1] -= current_fuel
                print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

    return garage


def refuel_func(current_car, current_fuel, garage):
    if current_car in garage:
        if garage[current_car][1] + current_fuel <= 75:
            garage[current_car][1] += current_fuel
            print(f"{current_car} refueled with {current_fuel} liters")
        else:
            needed_fuel = 75 - garage[current_car][1]
            garage[current_car][1] += needed_fuel
            print(f"{current_car} refueled with {needed_fuel} liters")

    return garage


def revert_func(current_car, kilometers, garage):
    if current_car in garage:
        garage[current_car][0] -= kilometers
        if garage[current_car][0] < 10000:
            garage[current_car][0] = 10000
        print(f"{current_car} mileage decreased by {kilometers} kilometers")

    return garage


def need_for_speed(number):
    garage = {}
    garage_func(number, garage)

    while True:

        command = input().split(' : ')

        if command[0] == 'Stop':
            for vehicle in garage:
                print(f"{vehicle} -> Mileage: {garage[vehicle][0]} kms, Fuel in the tank: {garage[vehicle][1]} lt.")
            break

        current_command = command[0]
        current_car = command[1]

        if current_command == 'Drive':
            distance = int(command[2])
            current_fuel = int(command[3])
            drive_func(current_car, distance, current_fuel, garage)

        elif current_command == 'Refuel':
            current_fuel = int(command[2])
            refuel_func(current_car, current_fuel, garage)

        elif current_command == 'Revert':
            kilometers = int(command[2])
            revert_func(current_car, kilometers, garage)


number = int(input())
need_for_speed(number)
