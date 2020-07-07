import sys

doc = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
doc = doc.replace(' ', '')
word = word.replace(' ', '')

length = len(doc)
cnt, i = 0 , 0

while 1:
    doc = doc[i:]
    if word in doc:
        cnt += 1
        i = doc.index(word)
        i += len(word)
    else:
        break
    if i >= length:
        break

print(cnt)
