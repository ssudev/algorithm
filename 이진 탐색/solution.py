# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 중간점인 경우
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# 이진 탐색 소스코드 구현(반복문)
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

n, target = list(map(int,input().split()))

array = list(map(int, input().split))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 없습니다.")
else:
    print(result + 1)