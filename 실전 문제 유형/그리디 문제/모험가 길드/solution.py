n = int(input())

array = list(map(int, input().split()))
max_sort_array = sorted(array, reverse=True)

result = 0

for max_num in max_sort_array:
    
    if n > 0:
        n -= max_num

        if n >= 0:
            result += 1
        else:
            break

print(result)