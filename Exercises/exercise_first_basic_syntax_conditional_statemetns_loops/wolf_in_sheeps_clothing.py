text = input()
wolf = 'wolf'
sheep = 'sheep'

text_as_list = [text]

for word in range(len(text_as_list)):
    if text_as_list[word] == wolf:
        print(text_as_list[word])