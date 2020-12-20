N, M, K = map(int, input().split())
number = list(map(int, input().split()))

number.sort()

first = number[-1:]
second = number[-2:-1]

answer = 0
num = 0

for _ in range(M):
    if num == K:
        answer += second[0]
        num = 0
    else:
        answer += first[0]
        num += 1

print(answer)
        
    