n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

edges = []
cost = []

for i in range(1,m+1):
    a,b,c = map(int, input().split())

    edges.append([c,a,b])

edges.sort()

for edge in edges:
    
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union(parent, edge[1], edge[2])
        cost.append(edge[0])

result = sum(cost) - cost[len(cost)-1]
print(result)