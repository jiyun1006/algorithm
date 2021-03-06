# greedy   

<br>


## 문제 해설(내 풀이, 정답 풀이) 

<br>


>### 모험가 길드   

<br>


- 내 풀이     

공포도를 기준으로 **작은 순서**로 정렬을 한 다음, **dict 자료형**에 넣은 다음,
순서대로 값을 뽑으면서, 사람을 채워나간다. 


```python
for i in ad_list:
    if int(i[0]) == 1:   # 공포도가 1이면 바로 그룹 수 추가하고 다른 멤버 조사.
        cnt += i[1]
        continue
    if int(i[0]) <= i[1]:  # 현재 공포도를 채울 인원이 있다면, 그 멤버들로 그룹결성.
        cnt += i[1]//int(i[0])
        tmp += i[1]%int(i[0])
    else:
        if int(i[0]) <= tmp:  # 현재 공포도를 채울 인원이 안된다면, 다음 공포도 멤버까지 고려.
            cnt += tmp//int(i[0])
            tmp = tmp%int(i[0])
        else:
            tmp += i[1]
```
*알고리즘 자체는 방향이 맞지만, 굳이 dict 자료형을 쓸 이유가 없음.*   

<br>

- 정답    

공포도를 기준으로 작은 순서로 정렬한 다음, 인원 수를 기록해나가며, 그룹 생성


```python
for ad in ad_list:
    tmp += 1     # tmp는 현재 결성하고 있는 그룹의 인원 수
    if tmp >= ad:  # 현재 결성중인 그룹의 인원수가 공포도를 충족시키면, 바로 그룹 수 추가.
        cnt += 1  # 
        tmp = 0
```
*****
<br><br>

>### 무지의 먹방 라이브   

<br>

- 내가 생각한 알고리즘   

시간을 음식 리스트 길이로 나눈 몫만큼 전체 배열에 빼준다음,
남은 시간만큼 배열을 돌아서 위치한 값을 결과로 내준다.

*효율성 측면에서 너무 안좋은 풀이.*   

<br>

- 정답   

우선순위 큐를 이용해서 가장 작은 시간을 가진 음식을 이용해서 
시간을 줄여나간다.   

```python
while total + ((q[0][0]- pre) * time_len) <= k:   
      ---> 음식먹는데 걸리는 시간과 배열 길이의 곱과 총 소모한 시간이 제한 시간보다 작을 때, 반복문 실행

        now = heapq.heappop(q)[0]  ---> 우선순위 큐에서 가장 작은 값을 빼면서 시간 계산
        
        total += (now - pre)* time_len   ---> 이전에 소모한 시간은 제외하고, 다시 총 소모시간 계산.
        time_len -= 1
        pre = now
```

*방향은 맞지만, 적절한 자료구조 사용 미흡.*



<br><br>
*****
*****
*****
<br><br><br>
