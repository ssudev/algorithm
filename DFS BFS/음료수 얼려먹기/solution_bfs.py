from collections import deque

def bfs(i,j,graph,visited,dx,dy):
    
    visited[i][j] = True
    que = deque([[i,j]])

    # que가 있을동안 반복
    while que:
        array = list(que.popleft())
        x, y = array[0], array[1]

        for k in range(4):
            x = x + dx[k]
            y = y + dy[k]

            if x >= 0 and x <= len(visited)-1 and y >= 0 and y <= len(visited[i])-1 and graph[x][y] == 0 and visited[x][y] == False:
                que.append([x,y])
                visited[x][y] = True
            
n, m = map(int, input().split())

graph = []
visited = [[False]*m for i in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = 0

for i in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(m):
        now = graph[i][j]

        if now == 0 and visited[i][j] == False:
            bfs(i,j,graph,visited,dx,dy)
            result += 1
            print(visited, i, j)

print(result)