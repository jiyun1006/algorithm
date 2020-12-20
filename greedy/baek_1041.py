import sys

N = int(sys.stdin.readline())

A, B, C, D, E, F = map(int, sys.stdin.readline().split())

value1 = min(
    list(map(sum, [[A, B], [A, C], [A, D], [A, E], [B, C], [B, D], [E, C], [E, D], [F, B], [F, C], [F, E], [F, D]])))
value2 = min(list(map(sum, [[A, B, C], [A, B, D], [A, E, D], [A, E, C], [F, B, C], [F, B, D], [F, E, C], [F, E, D]])))

one = ((N - 2) * (5 * N - 6))
two = (8 * N - 12)

if N == 1:
    print(sum([A, B, C, D, E, F]) - max([A, B, C, D, E, F]))
else:
    print(one * min([A, B, C, D, E, F]) + two * value1 + 4 * value2)

# 한 개면  0     9      28      57
#              (N-2)(N-1)*4 + (N-2)(N-2)
# 두 개면  4     8      12      16
#
# 세 개면  4     4       4        4
