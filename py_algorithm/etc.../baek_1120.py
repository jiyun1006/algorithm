import sys

x, y = map(str, sys.stdin.readline().strip().split())

min = 50
diff = len(y) - len(x)

if diff >= 1:
    for i in range(diff+1):
        count = 0
        for j in range(len(x)):
            if x[j] != y[j + i]:
                count += 1
        if min > count:
            min = count
    print(min)
else:
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    print(count)


