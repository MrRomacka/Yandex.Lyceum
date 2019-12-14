word = input().lower()
min_word = word
max_word = word

while True:
    word = input().lower()
    if word == 'стоп':
        break
    if len(word) > len(max_word):
        max_word = word
    if len(word) < len(min_word):
        min_word = word

if set(min_word) <= set(max_word):
    print("Yes")
else:
    print("No")