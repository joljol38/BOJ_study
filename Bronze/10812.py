# 10812번 : 바구니 순서 바꾸기

N, M = map(int, input().split())
list = [i+1 for i in range(N)]
# print(list)

for i in range(M):
    a, b, c = map(int, input().split())
    list = list[:a-1]+list[c-1:b]+list[a-1:c-1]+list[b:]
print(*list)