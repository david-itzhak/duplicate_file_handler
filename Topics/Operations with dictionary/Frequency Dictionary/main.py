words_count = {}
for word in input().lower().split():
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

for word, count in words_count.items():
    print(word, count)