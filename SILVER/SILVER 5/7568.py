N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])
    
for i in range(N):
    cnt = 1
    for j in range(N):
        if (lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]):
            cnt += 1
    print(cnt, end = " ")