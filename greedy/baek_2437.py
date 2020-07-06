import sys


N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

#####3
weight.sort()
sum = 0
for i in range(N):
    if sum + 1 >= weight[i]:
        sum += weight[i]
    else:
        break
print(sum+1)



######2
# from itertools import combinations
# value = [0]*1000000
# value[0] = 1
#
# for i in range(1, N):
#     weg = list(set(list(combinations(weight, i))))
#
#     for j in range(len(weg)):
#         if value[sum(weg[j])] != 0:
#             continue
#         else:
#             value[sum(weg[j])] += 1
#
# print(value.index(0))



#######1
# weight.sort()
#
# sum_num = 0
# sum_list = []
# for i in range(N):
#     sum_num += weight[i]
#     sum_list.append(sum_num + 1)
#
# for i in range(N):
#     value = sum_list[i]
#     weight_copy = weight.copy()
#     while value > 0:
#         value -= weight_copy[bisect(weight_copy, value) - 1]
#         weight_copy.pop(bisect(weight_copy, value) - 1)
#         if not weight_copy:
#             break
#     if value < 0:
#         print(sum_list[i])
#         break


# 1 1 2 3 6 7 30
