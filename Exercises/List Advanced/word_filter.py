text = input().split()
text_len_is_even = [word for word in text if len(word) % 2 == 0]
print('\n'.join(text_len_is_even))