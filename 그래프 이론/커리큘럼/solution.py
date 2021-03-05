from collections import deque

n = int(input())

graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
costs = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))

    costs[i] = data[0]

    for j in range(1, len(data)-1):
        graph[data[j]].append(i)
        indegree[i] += 1

q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append([i, costs[i]])

while q:
    a = q.popleft()
    now, cost = a[0], a[1]

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            costs[i] += cost
            q.append([i, costs[i]])

print(costs)