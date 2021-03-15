import heapq

def solution(food_times, k):
    q = []
    
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i+1])
        
    pre_time = 0
    now_time = 0
    sum_time = 0
    n = len(food_times)
    
    while k - (sum_time + (q[0][0] - pre_time)*n) >= 0:
        now_time, index = heapq.heappop(q)
        sum_time += (now_time-pre_time) * n
        pre_time = now_time
        n -= 1

        print(now_time, sum_time, pre_time, n)
    
        if not q:
            return -1
    
    result = sorted(q, key=lambda x:x[1])
    
    return result[(k-sum_time)%len(q)][1]

print(solution([3,1,2], 5))