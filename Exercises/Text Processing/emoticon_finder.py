text_for_searching = input()
for points in range(len(text_for_searching)):
    if text_for_searching[points] == ':':
        print(f':{text_for_searching[points + 1]}')