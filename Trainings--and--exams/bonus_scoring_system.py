from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_lectures = 0
maximum_student_bonus = 0

for student in range(number_of_students):
    current_student_attendance = int(input())
    max_bonus = ceil((current_student_attendance / number_of_lectures) * (5 + additional_bonus))
    if max_bonus > maximum_student_bonus:
        maximum_student_bonus = max_bonus
        max_lectures = current_student_attendance

print(f'Max Bonus: {maximum_student_bonus}.')
print(f'The student has attended {max_lectures} lectures.')
