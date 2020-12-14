def solution(N):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        count += N // coin
        N = N % coin

    return count

print(solution(1260))
print(solution(14720))



