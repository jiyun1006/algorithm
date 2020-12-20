from collections import deque


def solution(begin, target, words):
    answer = 0
    diff = deque()
    visit = [0 for _ in range(len(words))]

    def Dfs(diff, begin_word, words_list, re, visit):
        re += 1

        for n, word in enumerate(words_list):
            term = 0
            for i in range(len(begin_word)):
                if begin_word[i] != word[i]:
                    term += 1
            if term == 1 and visit[n] == 0:
                diff.append((words[n], n, re))
        if not diff:
            return 0

    if target not in words:
        return 0

    while begin != target:
        Dfs(diff, begin, words, answer, visit)
        if not diff:
            return 0
        visit[diff[0][1]] = 1
        answer = diff[0][2]
        begin = diff.popleft()[0]

    return answer