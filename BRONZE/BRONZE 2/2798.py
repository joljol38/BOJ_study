# 2798번 : 블랙잭

import itertools

N, M = map(int, input().split())
n = list(map(int, input().split()))
lsum = []
lmax = []
# print(n)

com = itertools.combinations(n, 3)
lcom = list(com)
# print(lcom)

for i in range(len(lcom)):
    lsum.append(sum(lcom[i]))
    
for number in lsum:
    if number <= M:
        lmax.append(number)

print(max(lmax))