import sys

N, M = map(int, sys.stdin.readline().split())
min_six, min_one = 1000, 1000
for i in range(M):
    six, one = map(int, sys.stdin.readline().split())
    min_six = min(min_six, six)
    min_one = min(min_one, one)

price = 0

if min_six > (min_one*6):
    min_six = (min_one*6)

if ((N % 6) * min_one) > min_six:
    price = (N // 6) * min_six + min_six
else:
    price = (N // 6) * min_six + (N % 6) * min_one

print(price)
