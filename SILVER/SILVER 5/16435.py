# 16435번 : 스네이크버드

N, L = map(int, input().split())

f = list(map(int, input().split()))
f.sort()

# print(f)
for i in range(len(f)):
    if L < f[i] :
        continue
    elif L > f[i] :
        L += 1
    else :
        L += 1
        
print(L)