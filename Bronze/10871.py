# 10871번 : X보다 작은 수
a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []

for i in c:
    if i < b:
        d.append(i)
        
print(*d)