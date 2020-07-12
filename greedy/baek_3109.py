import sys

R, C = map(int, sys.stdin.readline().split())


M = []
for i in range(R):
    M.append(list(sys.stdin.readline().rstrip()))



def pipe(i, j):
    global cnt, end
    if i == -1 or i == R:
        return
    if M[i][j] == 'x':
        return
    M[i][j] = 'x'

    if j == (C - 1):
        cnt += 1
        end = True
        return

    for k in i_list:
        pipe(i + k, j + 1)
        if end:
            return


i_list = [-1, 0, 1]
i, j = 0, 0
cnt = 0

for k in range(R):
    end = False
    pipe(i + k, j)

print(cnt)

# def pipe(p_list, i, j, sol_list):
#     if j == (C - 1):
#         return 0
#
#     if i == 0 or i == (R - 1):
#         if M[i][j + 1] == "x":
#             if M[i + 1][j + 1] == "x":
#                 pipe(M, i + 1, j, sol)
#             else:
#                 if (i + 1, j + 1) in sol:
#                     return
#                 else:
#                     sol.append((i + 1, j + 1))
#                     pipe(M, i + 1, j + 1, sol)
#         else:
#             if (i, j + 1) in sol:
#                 return
#             else:
#                 sol.append((i, j + 1))
#                 pipe(M, i, j + 1, sol)
#
#     else:
#         print("ss")
#         if M[i - 1][j + 1] == "x":
#             if M[i][j + 1] == "x":
#                 if M[i + 1][j + 1] == "x":
#                     pipe(M, i + 1, j, sol)
#                 else:
#                     if (i + 1, j + 1) in sol:
#                         pipe(M, i + 1, j, sol)
#                     else:
#                         sol.append((i + 1, j + 1))
#                         pipe(M, i + 1, j + 1, sol)
#             else:
#                 if (i, j + 1) in sol:
#                     if (i + 1, j + 1) in sol:
#                         pipe(M, i + 1, j, sol)
#                     else:
#                         sol.append((i + 1, j + 1))
#                         pipe(M, i + 1, j + 1, sol)
#                 else:
#                     sol.append((i, j + 1))
#                     pipe(M, i, j + 1, sol)
#         else:
#             if (i - 1, j + 1) in sol:
#                 if (i, j + 1) in sol:
#                     if (i + 1, j + 1) in sol:
#                         pipe(M, i + 1, j, sol)
#                     else:
#                         sol.append((i + 1, j + 1))
#                         pipe(M, i + 1, j + 1, sol)
#                 else:
#                     sol.append((i, j + 1))
#                     pipe(M, i, j + 1, sol)
#             else:
#                 sol.append((i - 1, j + 1))
#                 pipe(M, i - 1, j + 1, sol)


# 이미 존재하는 부분 제거 안함
# # sol에 넣을 부분 다시 생각
# pipe(M, i, j, sol)
# print(sol)
