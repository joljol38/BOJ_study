K, N = map(int, input().split())
lst = []
for i in range(K):
    lst.append(int(input()))
    
start = 1
end = max(lst)

while True:
    if (start > end):
        break
    
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):
        cnt += lst[i] // mid
    if (cnt >= N):
        start = mid + 1
    else:
        end = mid - 1
print(end)