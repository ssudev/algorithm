n = input()
f = 0
s = 0
for i in range(len(n)//2):
    f += int(n[i])

for i in range(len(n)//2,len(n)):
    s += int(n[i])

if f == s:
    print("LUCKY")
else:
    print("READY")