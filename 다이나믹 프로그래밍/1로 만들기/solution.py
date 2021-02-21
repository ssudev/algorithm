import sys

x = int(input())
dp = [0]*(x+1)

dp[1] = 0


for i in range(2, x+1):
    a,b,c,d = sys.maxsize,sys.maxsize,sys.maxsize,sys.maxsize

    if i % 5 == 0:
        a = dp[int(i/5)] + 1
    
    if i % 3 == 0:
        b = dp[int(i/3)] + 1
    
    if i % 2 == 0:
        c = dp[int(i/2)] + 1
    
    d = dp[i-1] + 1

    dp[i] = min(a,b,c,d)

print(dp)
