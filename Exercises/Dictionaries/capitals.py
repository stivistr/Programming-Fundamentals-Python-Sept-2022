countries = input().split(', ')
capitals = input().split(', ')

pairs = dict(zip(countries, capitals))

for pair in pairs.keys():
    print(f"{pair} -> {pairs[pair]}")
