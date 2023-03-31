# 10813번 : 공 바꾸기
N, M = map(int, input().split())
n_list = []

for i in range(N):
    n_list.append(i+1)
# print(n_list)

for j in range(M):
    a, b = map(int, input().split())
    temp = n_list[a-1]
    n_list[a-1] = n_list[b-1]
    n_list[b-1] = temp
print(*n_list)