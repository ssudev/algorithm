import heapq

n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int ,input().split())

    # 양방향
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int ,input().split())

for l in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][l] + graph[l][b])

distance = graph[1][k] + graph[k][x]

if distance > INF:
    print(-1)
else:
    print(distance)