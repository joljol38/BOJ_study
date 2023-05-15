import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
pre = [0]
cnt = 0

for i in range(N):
    cnt += arr[i]
    pre.append(cnt)

for j in range(M):
    a, b = map(int, input().split())
    print(pre[b] - pre[a-1])
