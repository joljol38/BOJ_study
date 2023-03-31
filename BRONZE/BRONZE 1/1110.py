# 1110 : 더하기 사이클

N = int(input())
num = N
cy = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    cy += 1
    
    if (num == N):
        break
    
print(cy)
