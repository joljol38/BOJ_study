N, M = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    tot = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            tot += x - mid
    if tot < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)