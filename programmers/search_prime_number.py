from itertools import permutations


def solution(numbers):
    answer = 0
    for i in range(1, len(numbers) + 1):
        a = list(set(list(map(''.join, permutations(numbers, i)))))
        for j in a:
            if j[0] == "0":
                continue
            prime = prime_num(int(j))
            if prime:
                answer += 1
    return answer


def prime_num(num):
    prime = False
    if num == 1:
        return prime
    for i in range(2, num + 1):
        if i == num:
            prime = True
            break
        if num % i == 0:
            break

    return prime