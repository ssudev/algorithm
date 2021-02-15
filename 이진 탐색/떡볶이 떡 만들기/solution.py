def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    sum_array = 0
    # 짜른 값
    for i in array:
        k = i - mid

        if k > 0:
            sum_array += k
    
    if sum_array == target:
        return mid
    elif sum_array > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

n, m = map(int,input().split())

h = list(map(int,input().split()))

start = 0
end = max(h)

print(binary_search(h, m, start, end))