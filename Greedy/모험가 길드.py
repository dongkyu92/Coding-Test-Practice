N = int(input())
group = list(map(int, input().split()))

# 오름차순 버전
answer = 0 # 총 그룹 수
count = 0 # 단위 그룹 수

group.sort()

for i in group:
    count += 1
    if count >= i:
        answer += 1
        count = 0
print(answer)

# 내림차순 버전
# group.sort(reverse=True)
# answer = []
# temp = []
# while True:
#     if len(group) == 0:
#         break
#     for i in range(group[0]):
#         temp.append(group.pop(0))
#     answer.append(temp)
# print(len(answer))

# N 모험가 수
# group 모험가 각각의 공포도  