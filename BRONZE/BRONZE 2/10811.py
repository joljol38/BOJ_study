# 10811번 : 바구니 뒤집기

N, M = map(int, input().split())
n_list = []
for i in range(N):
    n_list.append(i+1)
# print(n_list)

for j in range(M):
    a, b = map(int, input().split())
    n_list[a-1:b] = list(reversed(n_list[a-1:b]))
print(*n_list)