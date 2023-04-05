# 2475번 : 검증수
n = list(map(int, input().split()))
a = 0
for i in range(len(n)):
    a += (n[i]**2)
print(a%10)