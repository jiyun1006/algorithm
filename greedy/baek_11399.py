import sys

N = int(sys.stdin.readline())

order_list = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(order_list[0])
else:
    sum1, sum2 = 0, 0
    order_list.sort()
    for i in range(N):
        sum1 += order_list[i]
        sum2 += sum1

print(sum2)
