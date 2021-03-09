n = input()

cnt_0 = 0
cnt_1 = 0

for i in range(len(n)-1):

    if n[i] != n[i+1] and n[i] == "0":
        cnt_0 += 1
    elif n[i] != n[i+1] and n[i] == "1":
        cnt_1 += 1

if len(n) > 1:

    if n[-1] == "0" and n[-2] == "1":
        cnt_0 += 1
    elif n[-1] == "1" and n[-2] == "0":
        cnt_1 += 1

print(min(cnt_0, cnt_1))