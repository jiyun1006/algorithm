n = int(input())
# 개수 입력받기
op = input().split()
# 부등호 입력받기
c = [False] * 10
# 숫자 중복안되게 하기 위함.
mx, mn = "", ""


# max, min 구하기

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


# 부등호 성립하는지에 대한 함수

def solve(cnt, s):
    global mx, mn
    # 전역변수로 선언해서 밖의 변수를 가져온다.

    if cnt == n + 1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        # 0부터 9 까지 탐색하는 for 문
        if not c[i]:
            # 해당 숫자가 쓰였는지 아닌지 확인
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]):
                c[i] = True
                # 쓰인 숫자는 True로 바꿈
                solve(cnt + 1, s + str(i))
                c[i] = False


solve(0, "")
print("%s\n%s" % (mx, mn))
