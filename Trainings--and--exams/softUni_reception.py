first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
students_count = int(input())

students_helped_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
students_helped = 0
time_for_helping = 0


while students_count > students_helped:
    students_helped += students_helped_per_hour
    time_for_helping += 1
    if time_for_helping % 4 == 0:
        time_for_helping += 1

print(f"Time needed: {time_for_helping}h.")
