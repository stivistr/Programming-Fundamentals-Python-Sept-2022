usernames = input().split(', ')
for username in usernames:
    if 3 < len(username) < 16:
        if username.isalnum() or '_' in username or '-' in username:
            print(username)