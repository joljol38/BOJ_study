N = int(input())

d = [0, 1, 3]
for i in range(3, N + 1):
    d.append((d[i - 2]*2) + d[i - 1])


print(d[N] % 10007)