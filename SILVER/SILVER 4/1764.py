N, M = map(int, input().split())
nosee = []
nolisten = []
for _ in range(N):
    name = input()
    nosee.append(name)
for _ in range(M):
    name = input()
    nolisten.append(name)
    
inter = sorted(list(set(nosee) & set(nolisten)))
    
print(len(inter))
print(*inter, sep="\n")