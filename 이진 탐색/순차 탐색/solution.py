# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1


array = ['A', 'B', 'C', 'D', 'E']
n = 5
target = 'C'

print(sequential_search(n, target, array))