import math
from math import floor

biscuits_per_worker = int(input())
workers_count = int(input())
number_of_biscuits_from_competitor = int(input())

our_factory_production = 0
biscuits_per_day = biscuits_per_worker * workers_count

for day in range(30):
    if day % 3 == 0:
        biscuits_third_day = math.floor(biscuits_per_day * 0.75)
        our_factory_production += biscuits_third_day
    else:
        our_factory_production += biscuits_per_day

difference_between_companies = our_factory_production - number_of_biscuits_from_competitor
difference_as_percentage = difference_between_companies / number_of_biscuits_from_competitor * 100

print(f"You have produced {our_factory_production} biscuits for the past month.")

if difference_between_companies > 0:
    print(f'You produce {difference_as_percentage:.2f} percent more biscuits.')
else:
    print(f"You produce {abs(difference_as_percentage):.2f} percent less biscuits.")