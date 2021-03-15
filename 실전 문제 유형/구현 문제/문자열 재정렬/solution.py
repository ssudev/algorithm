n = input()
s = []
k = 0

for i in n:
    if i.isdigit():
        k += int(i)
    else:
        s.append(i)

s.sort()

print("".join(s) + str(k))