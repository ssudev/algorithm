n = int(input())
k = int(input())

apples = []

for i in range(k):
    apples.append(list(map(int, input().split())))

l = int(input())
rotates = []
for i in range(l):
    rotates.append(list(input().split()))

d = [[0,1],[1,0],[0,-1],[-1,0]]
position = 0

snake = []
snake.append([1,1])
result = 0

while True:
    result += 1
    dy, dx = snake[-1]
    dy += d[position][0]
    dx += d[position][1]

    for i in range(len(apples)):
        if apples[i] == [dy,dx]:
            snake.pop(0)
            apples.pop(i)
            break

    # 벽에 부딛히는 경우
    if dy > n or dy < 1 or dx > n or dx < 1:
        print("벽 : dy : " + str(dy) + "dx : "+ str(dx), snake)
        break
    
    # 몸에 부딛히는 경우
    if [dy,dx] in snake:
        print("몸 : dy : " + str(dy) + "dx : "+ str(dx), snake)
        break
    
    snake.append([dy,dx])
    print(snake, result)

    # 방향 전환
    for rotate in rotates:
        if result == int(rotate[0]):
            
            if rotate[1] == 'D':
                position += 1
            else:
                position -= 1
            
            if position == 4:
                position = 1
            elif position == -1:
                position = 3

            print(result, position)    

print(result)        