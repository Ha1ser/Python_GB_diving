text = sorted(input("введите текст: ").split())
# text.sort() сохранять в переменную не надо
max_length = 0
print(text)

for word in text:
    word_len = len(word)
    if max_length < word_len:
        max_length = word_len

for nn, word in enumerate(text, 1):
    print(f"{nn:>2}. {word:>{max_length}}")


