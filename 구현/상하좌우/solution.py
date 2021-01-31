def solution1(n, plans):
    x, y = 1, 1

    for plan in plans:
        if plan == 'R':
            if y + 1 <= n:
                y += 1
        elif plan == 'L':
            if y - 1 >= 1:
                y -= 1
        elif plan == 'U':
            if x - 1 >= 1:
                x -= 1
        elif plan == 'D':
            if x + 1 <= n:
                x += 1
    
    return x,y

def solution2(n, plans):
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move = ['L', 'R', 'U', 'D']

    for plan in plans:
        nx, ny = 0, 0
        for i in range(len(move)):
            if plan == move[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        x,y = nx,ny

    return x,y

n = int(input())
plans = input().split()

x, y = 1, 1



print(x, y)