import sys
from bisect import bisect

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

dp = [number[0]]

for i in range(1, n):
    if number[i] > dp[-1]:
        dp.append(number[i])
    else:
        dp[bisect(dp, number[i])] = number[i]

print(len(dp))
