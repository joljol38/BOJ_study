# 5585번 : 거스름돈

money = int(input()) # 입력값
count = 0
n = 1000-money # 거스름돈

coin_type = [500, 100, 50, 10, 5, 1]

for coin in coin_type :
    # print(coin)
    count += n // coin # 거슬러 줄 수 있는 동전 개수
    # print(count)
    n %= coin
print(count)