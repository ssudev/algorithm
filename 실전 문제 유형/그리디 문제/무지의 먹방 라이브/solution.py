def solution(food_times, k):
    answer = 0
    index = -1
    
    for i in range(1, k+2):
        index += 1
    
        if index == len(food_times):
            index = 0

        if food_times[index] != 0:
            food_times[index] -= 1
        elif food_times[index] == 0:
            temp_index = index
            
            while True:
                index += 1
                if index == len(food_times):
                    index = 0
                    
                if index == temp_index:
                    index = -1
                    break
                
                if food_times[index] != 0:
                    food_times[index] -= 1
                    break
        if index == -1:
            answer = -1
            return answer
            
    answer = index + 1
    
    return answer

print(solution([4,1,1,5],4))