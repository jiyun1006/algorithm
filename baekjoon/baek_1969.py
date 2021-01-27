import sys

N, M = map(int, sys.stdin.readline().split())
dna = [sys.stdin.readline().strip() for i in range(N)]
cnt = 0
dna_str = ""
for i in range(M):
    dis = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        dis[dna[j][i]] += 1
        cnt += 1
    cnt -= dis[max(dis, key=lambda x: dis[x])]
    dna_str = dna_str + max(dis, key=lambda x: dis[x])

print(dna_str)
print(cnt)



# dis = ""
# cnt2 = 0
#
# for i in range(M):
#     temp = []
#     for j in range(N):
#         temp.append(dna[j][i])
#     max_cnt = 0
#     value = ""
#     for k in temp:
#         cnt = temp.count(k)
#         if value == k:
#             continue
#         if max_cnt < cnt:
#             max_cnt = cnt
#             value = k
#             value2 = ord(k)
#         elif max_cnt == cnt:
#             if value2 > ord(k):
#                 value = k
#                 value2 = ord(k)
#     cnt2 += len(temp) - max_cnt
#
#     dis = dis + value
#
# print(dis)
# print(cnt2)
