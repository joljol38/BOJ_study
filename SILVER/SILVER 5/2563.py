# 2563번 : 색종이

arr = [[0 for col in range(100)] for row in range(100)]
count = 0

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    for j in range(100-(b+9), 100-(b-1)):
        for k in range(a-1, a+9):
            arr[j][k] = 1

for row in arr:
    for one in row:
        if one == 1:
            count += 1
print(count)