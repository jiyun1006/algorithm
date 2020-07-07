import sys

N, L = map(int, sys.stdin.readline().split())

pipe = [0] * 1001

loc = list(map(int, sys.stdin.readline().split()))

for i in loc:
    pipe[i] += 1

cnt = 0
while 1:
    cnt += 1
    bk = pipe.index(1)
    for i in range(L):
        if bk+i > 1000:
            break
        pipe[bk + i] = 0
    if 1 not in pipe:
        break
print(cnt)

# 1000개의 리스트에서 물 새는곳의 위치를 1로 바꾼다.
# 단, 바꿀 때 옆+L까지 같이 바꾼다.
# 최대 길이 넘어가면 break
