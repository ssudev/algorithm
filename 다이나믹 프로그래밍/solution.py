import math

def is_prime_number(n):
    array = [True for _ in range(n+1)]
    res = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:

            for j in range(i,n+1,i):
                array[j] = False
    

    for i in range(1,len(array)):
        if array[i]:
            res.append(i)

    return res

print(is_prime_number(10))