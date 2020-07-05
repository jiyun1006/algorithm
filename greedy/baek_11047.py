import sys

N_K = list(map(int, sys.stdin.readline().split()))

price = [int(sys.stdin.readline().strip()) for x in range(N_K[0])]
target = N_K[1]
count = 0

for i in range(N_K[0]):
    count += target//price[-1-i]
    target %= price[-1-i]

print(count)
