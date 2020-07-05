num = int(input())
words_list = []
for i in range(num):
    words = str(input())
    word_len = len(words)
    words_list.append((words, word_len))
words_list = list(set(words_list))


def word_sort(list):
    list.sort(key=lambda x: (x[1], x[0]))
    return list


word_sort(words_list)
for a in words_list:
    print(a[0])
