import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

J = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    heapq.heappush(J, [w, v])

W = []
for i in range(K):
    weight = int(sys.stdin.readline().strip())
    heapq.heappush(W, weight)

sum_v = []
sum_value = 0
for i in range(K):
    min_w = heapq.heappop(W)
    while J and min_w >= J[0][0]:
        [a, b] = heapq.heappop(J)
        heapq.heappush(sum_v, -b)

    if sum_v:
        sum_value -= heapq.heappop(sum_v)
    elif not J:
        break
print(sum_value)

    # sum_w = 0
# for i in range(K):
#     temp = sorted(J, key=lambda x: -x[:][1] if x[:][0] <= weight[i] else 1)
#     print(temp)
#     if weight[i] < J[0][0]:
#         continue
#     else:
#         sum_w += temp[0][1]
#         J.remove(temp[0])
# print(sum_w)

# J.sort(key=lambda x: (-x[:][1], x[:][0]))
#
# for i in range(K):
#     j = 0
#     while j < (N - 1):
#         if weight[i] < J[j][0]:
#             j += 1
#             continue
#         else:
#             sum_w += J[j][1]
#             J.pop(j)
#             j += 1
#             break
# print(sum_w)
