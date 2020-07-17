import sys

cal = sys.stdin.readline().strip().split("-")
sum = 0
for number in cal[0].split("+"):
    sum += int(number)

for number in cal[1:]:
    for i in number.split("+"):
        sum -= int(i)

print(sum)