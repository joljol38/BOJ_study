# 2566번 : 최댓값
arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
    
print(max(list(map(max, arr))))
xlist=[(i+1,j+1) for i in range(9) for j in range(9) if arr[i][j] == max(list(map(max, arr)))]
for x, y in xlist:
    print(x,y)       