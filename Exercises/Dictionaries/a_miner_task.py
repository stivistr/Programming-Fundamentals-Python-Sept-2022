miner_task = {}

while True:
    resource = input()

    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in miner_task.keys():
        miner_task[resource] = 0

    miner_task[resource] += quantity

for gems in miner_task.keys():
    print(f"{gems} -> {miner_task[gems]}")