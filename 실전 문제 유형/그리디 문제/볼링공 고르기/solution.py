import itertools

n, m = map(int,input().split())
data = list(map(int,input().split()))

result = 0

for x in itertools.combinations(data, 2):
    combin = list(x)
    if combin[0] != combin[1]:
        result += 1

array = [0]*11
for x in data:
    array[x] += 1

result = 0
for i in range(1,m+1):
    n -= array[i]
    result += array[i] * n

print(result)