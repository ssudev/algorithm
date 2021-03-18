n = input()
length = len(n)
result = 1000

for i in range(1,length//2+1):
    patten = ""
    cnt = 1
    pre = n[0:i]
    for j in range(i, length, i):
        if pre == n[j:j+i]:
            cnt += 1
        else:
            patten += str(cnt) + pre if cnt > 1 else pre
            pre = n[j:j+i]
            cnt = 1
    
    # 남아있는 마지막 문자열 처리
    patten += str(cnt) + pre if cnt > 1 else pre
    result = min(result, len(patten))

print(result)