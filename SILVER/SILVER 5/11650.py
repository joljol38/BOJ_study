# 11650번 : 좌표 정렬하기

N = int(input())
n = []
for i in range(N) :
    xy = list(map(int, input().split()))
    n.append(xy)
 
for x, y in sorted(n):
    print(x, y)