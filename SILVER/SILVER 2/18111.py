import sys
N, M, B = map(int, input().split())
house = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
highest, ans = 0, 1000000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if house[j][k] < i:
                min += (i - house[j][k])
            else:
                max += (house[j][k] - i)
    inven = max + B
    if inven < min:
        continue
    time = 2*max + min
    if time <= ans:
        ans = time
        highest = i
print(ans, highest)