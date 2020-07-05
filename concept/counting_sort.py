list = [1, 3, 2, 4, 3, 2, 5, 3, 1, 2, 3, 4, 4, 3, 5, 1, 2, 3, 5, 2, 3, 1, 4, 3, 5, 1, 2, 1, 1, 1]
count = [0 for x in range(5)]


def counting_sort(list):
    result = []
    for i in range(len(list)):
        count[list[i] - 1] += 1
    j = 1
    for a in count:
        for i in range(a):
            result.append(j)
        j += 1
    return result


counting_sort(list)

for i in range(len(result)):
    print(result[i], end="")

# '범위조건'이 정해져있는 경우에 한해서 굉장히 빠르다.