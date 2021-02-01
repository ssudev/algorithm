def solution1(x, y):
    cnt = 0
    if x - 2 >= 1 and y - 1 >= 1:
        cnt += 1
    if x - 2 >= 1 and y + 1 <= 8:
        cnt += 1
    if x + 2 <= 8 and y - 1 >= 1:
        cnt += 1
    if x + 2 <= 8 and y + 1 <= 8:
        cnt += 1
    if y - 2 >= 1 and x - 1 >= 1:
        cnt += 1
    if y - 2 >= 1 and x + 1 <= 8:
        cnt += 1
    if y + 2 <= 8 and x - 1 >= 1:
        cnt += 1
    if y + 2 <= 8 and x + 1 <= 8:
        cnt += 1

    return cnt

def solution2(x,y):
    moves = [[-2,-1], [-2,1], [2,-1], [2,1], [-1,-2], [1,-2], [-1,2], [1,2]]
    cnt = 0
    for move in moves:
        xx = x + move[0]
        yy = y + move[1]

        if xx <= 8 and xx >= 1 and yy <= 8 and yy >= 1:
            cnt += 1
    
    return cnt

n = str(input())

x = int(ord(n[0])) - 96
y = int(n[1])

print(solution2(x,y))