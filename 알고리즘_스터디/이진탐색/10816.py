# 10816 숫자카드 2

from collections import Counter

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

C = Counter(n)

for i in m:
    if i in C:
        print(C[i], end = ' ')
    else :
        print(0, end = " ")