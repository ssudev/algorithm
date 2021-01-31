# 단순히 큰 숫자 2개로 처리하는 경우
def solution1(n,m,k,array):
    array.sort()

    num1, num2 = array[-1], array[-2]

    sum_num = 0

    while True:
        # K만큼 가장 큰수 더하기
        for i in range(k):
            if m == 0:
                break
            sum_num += num1
            m -= 1
        if m == 0:
            break
        sum_num += num2
        m -= 1
    return sum_num

def solution2(n,m,k,array):
    array.sort()

    num1, num2 = array[-1], array[-2]

    sum_num = 0
    count = 0
    # k+1 번만큼의 반복이 생성 + 반복 이외의 나머지
    count = int(m / (k+1)) * k + int( m % (k+1))
    sum_num = count * num1
    sum_num += (m-count) * num2

    return sum_num

# N,M,K 입력
n,m,k = map(int, input().split())

# N개의 데이터 리스트
array = list(map(int, input().split()))

print(solution2(n,m,k,array))