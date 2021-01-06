N = list((input()))

answer = 1
for i in N:
    if int(i) == 0:
        continue
    else:
        answer *= int(i)

print(answer)
