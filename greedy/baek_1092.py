import sys

io = sys.stdin.readline
N = int(io())
crane = sorted(list(map(int, io().split())), key=lambda x: -x)

M = int(io())
box = sorted(list(map(int, io().split())), key=lambda x: -x)

cnt = 0

if crane[0] < box[0]:
    cnt = -1
else:
    while box:
        for i in crane:
            if not box:
                break
            if crane[-1] < box[-1]:
                crane.remove(crane[-1])
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        cnt += 1

print(cnt)