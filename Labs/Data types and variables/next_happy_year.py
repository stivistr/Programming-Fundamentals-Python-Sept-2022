year = int(input())
happy_next_year = False

while not happy_next_year:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_next_year = len(set_year) == len(str(year))

print(year)
