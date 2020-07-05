list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


def quicksort(list):
    if len(list) > 1:
        pivot = list[int(len(list) / 2)]
        left, mid, right = [], [], []
        for i in range(len(list)):
            if list[i] > pivot:
                right.append(list[i])
            elif list[i] < pivot:
                left.append(list[i])

        mid.append(pivot)

        return quicksort(left) + mid + quicksort(right)


    else:
        return list


quicksort(list)

# O(N*logN)
# 최악은 O(N^2)
