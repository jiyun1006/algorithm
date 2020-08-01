import sys

io = sys.stdin.readline

N = io()
cnt = 0

for i in range(1, int(N) + 1):
    if len(str(i)) <= 2:
        cnt += 1
    else:
        if int(str(i)[0]) - int(str(i)[1]) ==  int(str(i)[1]) - int(str(i)[2]):
            cnt += 1
        else:
            continue
print(cnt)


# 세자리수는 어떻게 판별할까