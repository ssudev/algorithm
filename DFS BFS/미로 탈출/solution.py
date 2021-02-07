from collections import deque

def bfs(x,y,graph):
    depth = 1

    que = deque([[x,y,depth]])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while que:
        array = que.popleft()
        x,y,depth = array[0],array[1],array[2]
        depth += 1
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx >= 0 and xx <= len(graph) - 1 and yy >= 0 and yy <= len(graph[0]) - 1 and graph[xx][yy] == 1 and (xx != 0 or yy != 0):
                graph[xx][yy] = depth
                que.append([xx,yy,depth])
                if xx == len(graph) - 1 and yy == len(graph[0]) - 1:
                    return
            
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

bfs(0,0,graph)

for i in range(len(graph)):
    print(graph[i])