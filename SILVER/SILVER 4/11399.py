N = int(input())
p = list(map(int, input().split()))
p.sort()
a = 0

for i in range(N):
    for j in range(i+1):
        a += p[j]
print(a)