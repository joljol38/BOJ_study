N = int(input())
step = []
for i in range(N):
    step.append(int(input()))
    
# print(step)

dp = [0] * len(step)

if (len(step) <= 2):
    print(sum(step))
else :
    dp[0] = step[0]
    dp[1] = step[0] + step[1]
    
    for i in range(2, len(step)):
        dp[i] = max(dp[i - 3] + step[i - 1]+step[i], dp[i - 2]+step[i])
    print(dp[-1])