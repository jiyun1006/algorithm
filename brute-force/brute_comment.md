# Brute_force   

<br>

## 문제 해설(내 풀이, 정답 풀이)

<br>

>## 게임 개발   

<br>

**N,M의 행렬에서 움직이는 캐릭터를 조작하는 문제**   

**특별한 알고리즘 없이 구현 위주로 품.**   

<br>

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    ---> 방향을 위해 미리 설정하면, 코드가 깔끔해짐.

while 1:
    if mp[row][col] == '0':  
        mp[row][col] = '1'     ----> 반복문안에서 행렬을 돌아다니며, 0이면 표시를 위해 1로 바꿈.
        
    turn_lf()    ---> 문제 조건에 따라 먼저 회전(따로 함수 만듬)
    
    tmp_x = row + dx[d]
    tmp_y = col + dy[d]    ---> 임의의 x,y에 방향대로 움직인 값 설정.
    
    if mp[tmp_x][tmp_y] != '1':   ---> 처음 가 본 방향이 1이 아니라면, 이동 횟수를 늘리고, 다시 방향탐색
        cnt += 1
        row = tmp_x
        col = tmp_y
        turn_cnt = 0
        continue
        
        
    else:   ---> 1이라면, turn한 횟수 늘리고, 다시 처음으로
        turn_cnt += 1
        
    if turn_cnt == 4:  ---> 4방향 모두 봤을 때, 갈 곳이 없으면, 뒤로
        tmp_x = row - dx[d]
        tmp_y = col - dy[d]
        
        if mp[tmp_x][tmp_y] == 0:
            row = tmp_x
            col = tmp_y
        
        else:   ---> 뒤로 못가면 반복 파괴.
            break
        turn_cnt = 0

```

*****

<br>
<br>

>## 문자열 압축(2020카카오)   

<br>

- 내가 푼 풀이   

<br>

**python for문에서 반복 단위를 늘려가며 단위마다의 줄어드는 길이 확인**   

**얼만큼 줄어드는지에 대한 잘못된 코드로, 답이 안나옴**   

```python
for j in range(1,length+1):
    idx, cnt = 0, 0
    tmp = ''
    cnt2 = 1   ---> 반복 횟수를 저장하는 변수
    for i in range(0, len(s)+1, j):
        if tmp != s[idx:i]:
            if tmp and cnt2 > 1:   ---> 2번 이상 반복되었다면, 실행
                cnt += j*(cnt2-1)-1  ---> 압축을 해서 줄어드는 길이를 저장하는 변수
          
                cnt2 = 1
        if tmp == s[idx:i]:
            cnt2 += 1
        tmp = s[idx:i]
        idx = i   

    if cnt2 > 1:     ----> 남은 문자열 중, 줄어드는 길이 저장.
        cnt += j*(cnt2-1)-1            
    cnt_list.append(cnt)
```   

<br>

- 풀이   

**알고리즘 자체는 동일하나, 문자열 자체를 저장함으로써 줄어드는 길이에 대한 복잡함 해소.**   

```python
for j in range(1,length+1):
    idx, cnt = 0, 1
    tmp = s[0:j]
    tmp2 = ''
    for i in range(j, len(s), j):
        if tmp == s[i:i+j]:
            cnt += 1    ---> 반복횟수 기록.
        else:
            tmp2 += str(cnt) + tmp if cnt >= 2 else tmp     ---> 반복횟수가 2회 이상이면, 해당 문자열 저장.
            tmp = s[i:i+j]
            cnt = 1

    tmp2 += str(cnt) + tmp if cnt >= 2 else tmp   ---> 남은 문자열 처리
    answer = min(answer, len(tmp2))
```
