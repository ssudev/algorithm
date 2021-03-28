from itertools import combinations

n,m = map(int, input().split())

chickens = []
houses = []

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j] == 2:
            chickens.append([i,j])
        elif a[j] == 1:
            houses.append([i,j])

comChickens = list(combinations(chickens,m))
answer = 1e9

for com in comChickens:
    temp_answer = 0
    for house in houses:
        hx,hy = house[0],house[1]
        temp_cost = 1e9
        for cx,cy in com:
            cost = abs(cx - hx) + abs(cy - hy)
            temp_cost = min(temp_cost,cost)
        temp_answer += temp_cost
    answer = min(temp_answer, answer)

print(answer)



