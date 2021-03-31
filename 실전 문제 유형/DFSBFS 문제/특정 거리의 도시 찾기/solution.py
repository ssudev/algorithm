from collections import deque

n,m,k,x = map(int,input().split())

roads = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    roads[a].append(b)


queue = deque([[x, 0]])

visit = [False] * (n+1)
visit[x] = True
result=[]

print(queue)
while queue:
    target, cost = list(queue.popleft())
    print(target, cost)

    if cost == k:
        result.append(target)

    if cost > k:
        break

    for road in roads[target]:
        if not visit[road]:
            queue.append([road, cost+1])
            visit[road] = True

print(result)