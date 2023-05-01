import itertools
N, M = map(int, input().split())
nlist = list(range(1,N+1))

p = itertools.combinations_with_replacement(nlist, M)

plist = list(p)
# print(*plist, sep = "\n")
for i in range(len(plist)):
    print(*plist[i])