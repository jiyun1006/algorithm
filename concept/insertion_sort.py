list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


def insertion_sort(list):
    temp = 0

    for i in range(1, len(list)):
        for j in range(i):
            if list[i - j] < list[i - j - 1]:
                temp = list[i - j]
                list[i - j] = list[i - j - 1]
                list[i - j - 1] = temp
            else:
                break

            print(list)


def insertion_sort2(list):
    temp = 0
    for i in range(len(list) - 1):
        j = i
        while (list[j] > list[j + 1]):
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
            j -= 1
        print(list)


insertion_sort2(list)

# 정렬이 많이 진행된 상태에서는 가장 빠른 정렬 방법(특수한 상황)
