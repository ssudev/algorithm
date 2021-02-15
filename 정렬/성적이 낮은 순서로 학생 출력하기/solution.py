n = int(input())
array = []

for i in range(n):
    k = input().split()

    array.append([k[0], int(k[1])])

#array.sort(key=lambda array:array[1])

array = sorted(array, key=lambda x:x[1])

print(array)