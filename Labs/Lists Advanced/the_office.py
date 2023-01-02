employee_happiness = list(map(int, input().split()))
happiness_factor = int(input())
happiness_multiplied = [person * happiness_factor for person in employee_happiness]
average_happiness = sum(happiness_multiplied) / len(employee_happiness)
happy_count = [happy for happy in happiness_multiplied if happy >= average_happiness]
not_happy_count = [happy for happy in happiness_multiplied if happy < average_happiness]
if len(happy_count) >= len(not_happy_count):
    print(f'Score: {len(happy_count)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_count)}/{len(employee_happiness)}. Employees are not happy!')
