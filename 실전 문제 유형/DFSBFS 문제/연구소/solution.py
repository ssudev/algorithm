from itertools import combinations
from collections import deque
import copy

n,m = map(int,input().split())
graph = [[0] * m for _ in range(n)]
safe = []
viruses = []

for i in range(n):
    array = list(map(int,input().split()))

    graph[i] = array

    for j in range(m):
        if array[j] == 0:
            safe.append([i,j])
        elif array[j] == 2:
            viruses.append([i,j])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0

for com_safe in combinations(safe, 3):
    temp_graph = copy.deepcopy(graph)
    cnt = 0

    for x,y in list(com_safe):
        temp_graph[x][y] = 1

    queue = deque(viruses)
    while queue:
        array = queue.popleft()
        x,y = array[0], array[1]
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if (xx >= 0 and xx < n) and (yy >= 0 and yy < m) and temp_graph[xx][yy] == 0:
                queue.append([xx,yy])
                temp_graph[xx][yy] = 2

    for x in range(n):
        for y in range(m):
            if temp_graph[x][y] == 0:
                cnt += 1

    result = max(result,cnt)

print(result)