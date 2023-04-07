# 2755번 : 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input()) # floor
    n = int(input()) # door
    floor0 = [i for i in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            floor0[j] += floor0[j-1]
    print(floor0[-1])