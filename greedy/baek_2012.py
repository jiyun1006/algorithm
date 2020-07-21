import sys

N = int(sys.stdin.readline())

temp = sorted(int(sys.stdin.readline()) for _ in range(N))

# enumerate 사용
sum_list = sum(abs((i+1)- value) for i , value in enumerate(temp))
print(sum_list)
