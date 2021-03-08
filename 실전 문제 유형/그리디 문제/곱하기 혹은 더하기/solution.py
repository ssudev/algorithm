s = input()
result = int(s[0])


for i in range(1, len(s)):
    num = int(s[i])

    if result + num > result * num:
        result += num
    else:
        result *= num

print(result)