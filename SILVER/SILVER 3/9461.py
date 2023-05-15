T = int(input())
arr = [0, 1, 1, 1]
for i in range(1, 100):
    arr.append(arr[i] + arr[i + 1])
    
for _ in range(T):
    N = int(input())
    print(arr[N])