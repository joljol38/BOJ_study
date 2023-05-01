import itertools
N, M = map(int, input().split())
nlist = sorted(list(map(int, input().split())))


p = itertools.permutations(nlist, M)

plist = list(p)
# print(*plist, sep = "\n")
for i in range(len(plist)):
    print(*plist[i])