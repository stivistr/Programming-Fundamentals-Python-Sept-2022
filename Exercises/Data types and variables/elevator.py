persons = int(input())
elevator_capacity = int(input())

elevator_courses = persons // elevator_capacity
if persons % elevator_capacity != 0:
    elevator_courses += 1
print(elevator_courses)