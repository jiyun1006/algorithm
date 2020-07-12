import sys
S = sys.stdin.readline().rstrip()
S_z = S.split("1")
S_z = [x for x in S_z if x != '']
S_o = S.split("0")
S_o = [x for x in S_o if x != '']

if len(S_z) < len(S_o):
    print(len(S_z))
else:
    print(len(S_o))

