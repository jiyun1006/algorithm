import sys

N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()
temp = []
temp_k = K


for i in range(N):
    while temp and number[i] > temp[-1] and temp_k != 0:
        del temp[-1]
        temp_k -= 1
    temp.append(number[i])

print(''.join(temp[:N-K]))