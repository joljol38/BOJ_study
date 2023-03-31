# 2720번 : 세탁소 사장 동혁

T = int(input())
c = []
coin_type = [25, 10, 5, 1]
for i in range(T):
    C = int(input())
    for coin in coin_type :
        # print(coin)
        c.append(C // coin) # 거슬러 줄 수 있는 동전 개수
        # print(count)
        C %= coin
    # print(c)
    
matrix = [c[i:i+4] for i in range(0, len(c), 4)]
for row in matrix:
    print(*row)