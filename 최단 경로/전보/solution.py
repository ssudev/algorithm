import heapq

n, m, c = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(1,m+1):
    x,y,z = map(int, input().split())

    graph[x].append([y,z])

INF = int(1e9)
distance = [INF] * (n+1) 

def dj(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[0] = 0
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dj(c)
print(max(distance))