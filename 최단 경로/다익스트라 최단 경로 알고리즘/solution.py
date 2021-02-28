import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한대를 의미 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])

print(graph)

def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))    
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:

        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 거리가 더 길다면 무시
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
    print(distance[i])