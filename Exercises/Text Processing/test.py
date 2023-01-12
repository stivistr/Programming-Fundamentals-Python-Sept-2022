text = 'aSd2&5s@1'
for num in range(len(text)):
    if text[num].isdigit():
        text_till_number = text[0:len(text[num - 1])]
        print(text_till_number)