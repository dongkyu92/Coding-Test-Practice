N, K = map(int, input().split())
answer = 0

while True:
    if N == 1:
        break

    if N % K == 0:
        N = N // K
        answer += 1
    else:
        N -= 1
        answer += 1
print(answer)

    