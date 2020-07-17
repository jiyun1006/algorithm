import sys

pol = sys.stdin.readline().rstrip().split('.')
sum_list = []


if len(pol) == 1:
    if len(pol[0]) % 2 != 0:
        sum_list = ['-1']
    else:
        a = len(pol[0]) // 4
        b = (len(pol[0]) % 4) // 2
        sum_list.append('AAAA' * a + 'BB' * b)
else:
    for i in range(len(pol)):
        if pol[i] == '':
            sum_list.append('.')
            continue
        if len(pol[i]) % 2 != 0:
            sum_list = ['-1']
            break
        else:
            a = len(pol[i]) // 4
            b = (len(pol[i]) % 4) // 2
            sum_list.append('AAAA' * a + 'BB' * b)
            sum_list.append('.')

if len(sum_list) >1:
    sum_list.pop()


print(''.join(sum_list))
