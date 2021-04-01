from collections import deque

n,k = map(int,input().split())

graph = [[0] * n for _ in range(n)]
data = []
for i in range(n):
    graph[i] = list(map(int,input().split()))

    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])

s,x,y = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

data.sort()
queue = deque(data)

while queue:
    virus,sec,a,b  = queue.popleft()

    if sec == s:
        break

    for d in range(4):
        aa = a + dx[d]
        bb = b + dy[d]

        if aa >= 0 and aa < n and bb >= 0 and bb < n and graph[aa][bb] == 0:
            queue.append([virus, sec+1, aa,bb])
            graph[aa][bb] = virus

print(graph[x-1][y-1])