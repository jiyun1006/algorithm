num = int(input())
serial = []
for i in range(num):
    number = str(input())

    sum = 0
    for j in number:
        if j.isdigit():
            sum += int(j)

    serial.append((number, sum))

serial = list(set(serial))

serial.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in range(len(serial)):
    print(serial[i][0])


