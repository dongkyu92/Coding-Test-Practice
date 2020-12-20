N, M, K = map(int, input().split())
number = list(map(int, input().split()))

number.sort()
first = number[N - 1]
second = number[N - 2]

answer = 0
num = 0

for _ in range(M):
    if num == K:
        answer += second
        num = 0
    else:
        answer += first
        num += 1

print(answer)
        

# 가장 큰 수가 더해지는 횟수 계산

# count = int(M / (K + 1)) * K
# count += M % (K + 1)

# result = 0
# result += (count) * first
# result += (M - count) * second
