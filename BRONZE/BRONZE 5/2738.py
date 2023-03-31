# 2738번 : 행렬 덧셈
N, M = map(int, input().split())
arr1 = []
arr2 = []
for i in range(N):
    arr1.append(list(map(int, input().split())))

for j in range(M):
    arr2.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        print(arr1[row][col] + arr2[row][col], end = ' ')
    print()