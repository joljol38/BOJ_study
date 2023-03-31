# 1546번 : 평균

a = int(input())
b = list(map(int, input().split()))
c = []

for i in range(a):
    c.append(b[i]/max(b)*100)

print(sum(c)/len(c))