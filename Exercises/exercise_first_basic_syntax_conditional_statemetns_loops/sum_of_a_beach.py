text = input()

sand = 'sand'
water = 'water'
fish = 'fish'
sun = 'sun'

word_in_text = 0

if sand in text.lower():
    word_in_text += text.lower().count(sand)
if water in text.lower():
    word_in_text += text.lower().count(water)
if fish in text.lower():
    word_in_text += text.lower().count(fish)
if sun in text.lower():
    word_in_text += text.lower().count(sun)


print(word_in_text)