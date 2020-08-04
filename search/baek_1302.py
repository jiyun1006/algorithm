import sys

ip = sys.stdin.readline
temp = dict()
N = int(ip())
temp2 = list()

for i in range(N):
    v = ip().rstrip()
    if v in temp:
        temp[v] += 1
    else:
        temp[v] = 1

for i in temp.keys():
    if temp[i] == max(temp.values()):
        temp2.append(i)
temp2.sort()
print(temp2[0])

# temp2.append(max(temp))
# value = temp[max(temp)]
# temp.pop(max(temp))
#
#
# while value in temp.values():
#     temp2.append(max(temp))
#     temp.pop(max(temp))
#
# temp2.sort()
# print(temp2[0])