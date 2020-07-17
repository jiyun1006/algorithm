import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().strip().split()))
temp = [0] * (N - 1)

number.sort()
j = 0

for i in range(1, N):
    temp[j] = number[i] - number[i - 1]
    j += 1

temp.sort()

for i in range(K-1):
    if len(temp) == 0:
        break
    temp.pop()

print(sum(temp))
