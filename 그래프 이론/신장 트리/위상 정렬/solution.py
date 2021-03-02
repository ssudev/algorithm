from collections import deque

v, e = map(int, input().split())

graph = [[] for i in range(v+1)]

# 진입 차수
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(indegree):
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    return result

array = topology_sort(indegree)
print(array)