import sys

N = int(sys.stdin.readline())

ch_list = [""] * N

for i in range(N):
    ch_list[i] = sys.stdin.readline().rstrip()

value = []
temp = ""

if N == 2:
    print(3)
else:
    if ch_list.index("KBS1") == 0:
        for i in range(ch_list.index("KBS2")):
            value.append("1")
        for i in range(1, ch_list.index("KBS2")):
            value.append("4")
        print(''.join(value))

    else:
        for i in range(ch_list.index("KBS1")):
            value.append("1")
        for i in range(ch_list.index("KBS1")):
            value.append("4")
            temp2 = ch_list.index("KBS1")
            temp = ch_list[temp2]
            ch_list[temp2] = ch_list[temp2 - 1]
            ch_list[temp2 - 1] = temp
        if ch_list.index("KBS2") == 1:
            print(''.join(value))

        else:
            for i in range(ch_list.index("KBS2")):
                value.append("1")
            for i in range(1, ch_list.index("KBS2")):
                value.append("4")
            print(''.join(value))

# A B C D A B  3
# B C D A A B  2
# print(ch_list.index('KBS1'))
