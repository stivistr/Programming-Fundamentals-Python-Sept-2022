followers = {}

while True:

    command = input().split(': ')

    if command[0] == 'Log out':
        break

    current_command = command[0]
    username = command[1]

    if current_command == 'New follower':
        if username not in followers:
            followers[username] = [0, 0]

    elif current_command == 'Like':
        likes_count = int(command[2])
        if username in followers:
            followers[username][0] += likes_count
        else:
            followers[username] = [likes_count, 0]

    elif current_command == 'Comment':
        if username in followers:
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]

    elif current_command == 'Blocked':
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")
for follower in followers:
    print(f"{follower}: {sum(followers[follower])}")