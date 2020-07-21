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

# value = hw[0][0]
# i = 0
# ans = hw[0][1]
# while 1:
#     if hw[i][0] == value:
#         i += 1
#         continue
#     else:
#         value = hw[i][0]
#         ans += hw[i][1]
#
#     if value == max(hw)[0]:
#         break
#     i += 1
#
# print(ans)


# hw = sorted((list(map(int, sys.stdin.readline().split())) for i in range(N)), key=lambda x: (x[0], -x[1]))
#
# value = hw[0][0]
# i = 2
# ans = hw[0][1]
#
# j = 0

# while 1:
#     if hw[:][0].index(i):
#         print(hw[:][0].index(i))
#         j += 1
#     else:
#         j += 1
#     if j == 5:
#         break

# print(ans)
