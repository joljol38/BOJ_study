# 10810번 : 공넣기
N, M = map(int, input().split())
n_list = [0 for i in range(N)]

for j in range(M) :
    a, b, c = map(int, input().split())
    n_list[a-1:b] = [c for i in range(b-a+1)]
print(*n_list)