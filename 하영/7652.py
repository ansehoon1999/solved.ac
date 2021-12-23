from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs(x1,y1, x2,y2) :
  queue = deque()
  queue.append([x1,y1])
  visited[x1][y1] = 1
  while queue :
    a, b = queue.popleft()
    if a==x2 and b ==y2 :
      print(visited[x2][y2]-1)
      return
    for i in range(len(dx)) : 
      nx = a + dx[i]
      ny = b + dy[i]
      if 0<= nx <n and 0<=ny <n and visited[nx][ny]==0:
          queue.append([nx, ny])
          visited[nx][ny] = visited[a][b] +1

testCase = int(input())
while testCase >0 :
  testCase -=1
  n = int(input())
  x1, y1 = map(int, input().split())
  x2, y2 = map(int, input().split())
  visited = [[0] *n for _ in range(n)]
  bfs(x1, y1, x2, y2)