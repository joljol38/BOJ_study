import math

N = int(input())
dp = [0]*(N + 1)
dp[0], dp[1] = 0, 1

for i in range(2, N + 1):
    minv = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minv = min(minv, dp[i - j**2])
    dp[i] = minv + 1
print(dp[N])