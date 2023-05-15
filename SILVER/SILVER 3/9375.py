T = int(input())

for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        name, cloth = input().split()
        if cloth in clothes:
            clothes[cloth] += 1
        else:
            clothes[cloth] = 1
    cnt = 1
    for key in clothes:
        cnt *= (clothes[key] + 1)
    print(cnt - 1)