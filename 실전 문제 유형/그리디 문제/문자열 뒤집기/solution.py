n = input()

cnt_0 = 0
cnt_1 = 0
reverse_s = ""

for s in n:
    if s == "0":
        cnt_0 += 1
    else:
        cnt_1 += 1

if cnt_0 >= cnt_1:
    reverse_s = "1"
else:
    reverse_s = "0"

result = 0

for i in range(1,len(n)):
    
    if n[i] == reverse_s and n[i-1] != reverse_s:
        result += 1 

print(result)