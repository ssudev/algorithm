# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1

    for i in range(1,n+1):
        result *= i
    
    return result

def factorial_recursive(n):

    if n == 1:
        return 1
    
    return n * factorial_recursive(n-1)

def recursive(i):
    if i == 10:
        return
    print(i, "번째 재귀 함수에서 ", i+1, "번째 재귀 함수를 호출합니다.")
    recursive(i+1)
    print(i, "번째 재귀 함수 호출을 종료합니다.")

print(factorial_recursive(5))
print(recursive(1))