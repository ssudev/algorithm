array = [7,5,9,0,3,1,6,2,4,8,5]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        print(array, left, right,end= ' ')

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        
        print(array)
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


def quick_sort2(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할 왼쪽
    right_side = [x for x in tail if x > pivot] # 분할 오른쪽

    print("left : ", left_side)
    print("right : ", right_side)

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

#quick_sort(array, 0, len(array)-1)
print(quick_sort2(array))
