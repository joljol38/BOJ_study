N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))
dic = {}

for i in m:
    dic[i] = 0
for x in n:
    if x in dic:
        dic[x] = 1
for j in dic:
    print(dic[j], end = ' ')