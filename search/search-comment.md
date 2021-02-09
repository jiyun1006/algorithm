## Search   

<br>

## 문제해설(내 풀이, 정답 풀이)   
<br>

>## 미로 탈출   
>전형적인 bfs를 이용한 경로 찾는 문제이다.    
>아직 bfs를 다양하게 응용하지는 못하므로, 기본 문제부터 차근차근   

<br>

**행렬로 나타났지만, 그래프로 바꿔서 경로를 찾듯이 풀었다.**   

<br>

```python
from collections import deque

N, M = map(int, input().split())

maze = [list(map(int,input())) for _ in range(N)]

# 이동할 네 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
  queue = deque()
  queue.append((x,y))

  while queue:
      x , y = queue.popleft()
      
      # 방향별로 돌아가며 진행
      for i in range(len(dx)):
      
          # 좌표 수정
          nx = x + dx[i]
          ny = y + dy[i]
          
          # 벽에 닿거나, 행렬 범위를 벗어나면 바로 종료.
          if nx <= -1 or ny <= -1 or nx >=N or ny>= M or maze[nx][ny] == 0:
              continue
          
          # 길을 들어섰다면, 계속해서 지나온 경로의 수 만큼 기록해준다.
          if maze[nx][ny] == 1:
              maze[nx][ny] = maze[x][y] + 1
              queue.append((nx,ny))
  
  #마지막 도착지점에서의 경로의 수를 반환한다.
  return maze[N-1][M-1]
    

print(bfs(0,0))
```

<br><br>

>## 특정 거리의 도시 찾기 (백준 18352)   
>#### bfs알고리즘을 이용해서 이동하는 노드에 계속해서 거리를 더해간다.   
>#### 노드의 개수가 300,000개이고, 간선의 개수도 1,000,000이므로 bfs로 해결 가능하다.   

<br>

**중요한 건, 출발 도시는 거리를 0으로 생각해야 된다.(이것 때문에 오래 걸림)**   

**처음 나온 도로의 정보를 그래프로 바꾼다.**   

<br>

```python
N, M, K, X = map(int,input().split())

# 도로의 정보를 그래프로 바꾸는 과정 (0번 도시는 없기 때문에, 길이를 하나 더 추가한다.)
road = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    road[s].append(e)


q = deque([X])

# 모든 도시의 거리를 -1로 초기화
dist = [-1] * (N+1)

# 하지만 주어진 현재 도시 정보로 현재 도시는 거리를 0으로
dist[X] = 0


# bfs 
while q:
    tmp = q.popleft()
    for i in road[tmp]:
        if dist[i] == -1:
            dist[i] = dist[tmp] + 1
            q.append(i)
    

ans = False
for idx,i in enumerate(dist):
    if i == K:
        print(idx)
        ans = True

if not ans:
    print(-1)
       
```

<br><br>


>## 
