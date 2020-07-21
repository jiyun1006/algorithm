import sys

N = int(sys.stdin.readline())

temp = [0] * N
sum_list = 0

for i in range(N):
    a = int(sys.stdin.readline())
    temp[i] = a
temp.sort()
temp2 = [0] * N

for i in range(1, N + 1):
    temp2[i-1] = abs(temp[i-1] - i)

print(sum(temp2))


