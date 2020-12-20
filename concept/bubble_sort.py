list = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


def bubble_sort(list):
    temp = 0
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
        print(list)


bubble_sort(list)

# O(N^2)
# 버블정렬은 선택정렬보다 느리다 --> 시간복잡도는 똑같지만
# 계속해서 양옆의 수를 바꾸는 작업을 하기 때문에, 더 비효율적이다.

