N = int(input())
days = []
for i in range(N):
    days.append(list(map(int, input().split())))
# print(days)

dp = [0] * (len(days)+1)

for i in range(len(days)):
    for j in range(i + days[i][0], len(days)+1):
        if dp[j] < dp[i] + days[i][1]:
            dp[j] = dp[i] + days[i][1]
print(dp[-1])