# 11047번 : 동전 0
coin = []
new = []
count = 0
N, K = map(int, input().split())

for i in range(N):
    c = int(input())
    coin.append(c)
    new = coin[::-1]
# print(new)

for coin in new:
    count += K // coin
    K %= coin
print(count)
