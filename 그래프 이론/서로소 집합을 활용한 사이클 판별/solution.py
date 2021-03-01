# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    # 자기 자신을 부모로 갖고 있으면 루트 노드
    if parent[x] != x:
        # 부모 노드를 새로 갱신 => 경로 압축
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 초기화
parent = [0] * (v + 1)

# 처음 부모는 자기 자신
for i in range(1, v+1):
    parent[i] = i

# union 연산을 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

c = parent[1]
cycle = True

for i in range(1, v + 1):
    if c != parent[i]:
        cycle = False
        break

if cycle:
    print("싸이클")
else:
    print("no 싸이클")