import sys

bill = 1000

extra_money = [500, 100, 50, 10, 5, 1]

price = int(sys.stdin.readline())

target = bill - price
count = 0
for money in extra_money:
    count += int(target//money)
    target = target%money

print(count)
