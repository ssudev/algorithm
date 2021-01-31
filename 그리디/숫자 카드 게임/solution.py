n,m = map(int,input().split())
result = 0

for i in range(n):
    array = list(map(int, input().split()))

    l = min(array)

    # 둘중에 큰 값 찾기
    result = max(l,result)

print(result)