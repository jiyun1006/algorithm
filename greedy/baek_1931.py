import sys

N = int(sys.stdin.readline())

time = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
time.sort(key=lambda x: (x[1], x[0]))
end_time = 0
count = 0
for a in time:
    if end_time <= a[0]:
        end_time = a[1]
        count += 1
print(count)
