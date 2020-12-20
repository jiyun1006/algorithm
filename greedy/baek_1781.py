import sys
import heapq

# 따로따로 나눠서 map 메소드 쓰고 그 다음에 리스트에 넣는게 제일 빠름
# 리스트는 되도록이면 append 말고 미리 0으로 생성하기.

input = sys.stdin.readline

N = int(input())
hw_list = [0] * N
for i in range(N):
    d, value = map(int, input().rstrip().split())
    hw_list[i] = (d, value)

hw_list.sort()

data = []
for d, value in hw_list:
    heapq.heappush(data, value)
    if len(data) > d:
        heapq.heappop(data)

print(sum(data))

