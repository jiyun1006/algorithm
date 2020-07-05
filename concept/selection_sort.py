list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        temp = 0
        index = i
        for j in range(i + 1, len(list)):
            if min > list[j]:
                min = list[j]
                index = j
        temp = list[i]
        list[i] = min
        list[index] = temp

        print(list)


selection_sort(list)

# O(N^2)
