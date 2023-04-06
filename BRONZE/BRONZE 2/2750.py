N = int(input())
n = []
for i in range(N):
    a = int(input())
    n.append(a)


print(*sorted(n), sep = '\n')