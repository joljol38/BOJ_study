# 2108번 : 통계학

from collections import Counter

N = int(input())
n = []
for i in range(N):
    a = int(input())
    n.append(a)
# print(n)
n.sort()

print(int(round(sum(n)/N, 0))) # mean  
print(n[(N//2)]) # median

# mode
counter = Counter(n)
a = counter.most_common()

if len(n) > 1:
    if a[0][1] == a[1][1]:
        print(a[1][0])
    else:
        print(a[0][0])
else:
    print(n[0])

print(n[-1] - n[0])