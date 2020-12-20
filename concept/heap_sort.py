list = [7, 6, 5, 8, 3, 5, 9, 1, 6]


def heap_sort(list):
    j = 1
    for i in range(1, len(list)):
        ch = i
        temp = 0
        while 1:
            root = int((ch - 1) / 2)
            if list[root] < list[ch]:
                temp = list[root]
                list[root] = list[ch]
                list[ch] = temp

            ch = root

            if ch == 0:
                break

    while j != 9:
        temp = list[len(list) - j]
        list[len(list) - j] = list[0]
        list[0] = temp
        index = 0
        max = list[0]
        for k in range(0, len(list) - j):
            if max < list[k]:
                max = list[k]
                index = k

        temp = list[0]
        list[0] = list[index]
        list[index] = temp
        j += 1
    return list


heap_sort(list)

# O(N*logN)
# 또 다른 리스트를 생성하지 않기 때문에 메모리 측면에서 병합정렬보다 좋다.
# 속도는 퀵정렬이 평균적으로 더 빠르다.






