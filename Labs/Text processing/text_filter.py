banned_words = input().split(', ')
received_text_with_words_to_ban = input()

for word in banned_words:
    received_text_with_words_to_ban = received_text_with_words_to_ban.replace(word, len(word) * '*')

print(received_text_with_words_to_ban)
