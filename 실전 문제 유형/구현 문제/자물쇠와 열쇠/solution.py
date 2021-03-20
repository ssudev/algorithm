# 2차원 배열 90도 회전
def rotate(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    
    return result

def check(new_lock, n):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for k in range(4):
        
        key = rotate(key)
        
        for x in range(n*2):
            for y in range(n*2):
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock, n):
                    return True
    
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key, lock)


new_lock = [[0]*4 for _ in range(1)]
print(new_lock)
print(len(new_lock))