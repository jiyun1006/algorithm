>## Search   

<br><br>

>## 문제해설(내 풀이, 정답 풀이)   
<br>

>### 미로 탈출   
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
