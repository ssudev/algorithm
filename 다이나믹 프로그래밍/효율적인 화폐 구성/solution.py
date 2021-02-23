n, m = map(int,input().split())

money = []

for i in range(n):
    money.append(int(input()))

dp = [0] * (m+1)

for i in money:
    if i <= m:
        dp[i] = 1

for i in range(1,m+1):
    if dp[i] == 1:
        continue
    
    k = 10001
    for j in money:
        if i - j > 0:
            l = i - j
            s = dp[l] + dp[i-l]
            k = min(s,k)
    
    dp[i] = k

print(dp)