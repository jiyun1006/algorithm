import sys
N = list(sys.stdin.readline().strip())
if "0" not in N:
    print(-1)
else:
    N = [int(N) for N in N]
    if int(str(sum(N))+"0")%30 == 0:
        N = [str(N) for N in N]
        N.sort(reverse=True)
        sum = ""
        for num in N:
            sum = sum + num
        print(sum)
    else:
        print(-1)




