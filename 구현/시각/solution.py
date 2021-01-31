def solution1(n):
    hour = 0
    min = 0
    sec = 0
    cnt = 0

    while True:
        if hour == n+1:
            break

        sec += 1

        if sec == 60:
            sec = 0
            min += 1
        
        if min == 60:
            min = 0
            hour += 1
        
        k = str(hour) + str(min) + str(sec)

        if '3' in k:
            cnt += 1
            
    return cnt

# 시 분 초 3중 for문 구현
def solution2(n):
    cnt = 0
    for i in range(n+1):
        for j in range(60):
            for l in range(60):
                if '3' in str(i) + str(j) + str(l):
                    cnt += 1

n = int(input())


