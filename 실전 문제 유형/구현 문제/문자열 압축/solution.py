n = input()
length = len(n)
result = 1000

for i in range(1,length//2+1):
    patten = ""
    cnt = 1
    for j in range(0, length - i, i):
        if n[j:j+i] == n[j+i:j+2*i]:
            cnt += 1
        else:
            if cnt == 1:
                patten += n[j:j+i]
            else:
                patten += str(cnt) + n[j:j+i]
            
            cnt = 1
    print(patten, cnt)