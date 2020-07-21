import sys

N = int(sys.stdin.readline())

line = sorted((int(sys.stdin.readline()) for i in range(N)), key=lambda x: -x)

sum_list = sum(value - i for i, value in enumerate(line) if value - i > 0)
print(sum_list)
