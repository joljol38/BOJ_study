# 11021번 : A+B - 7
a = int(input())

for i in range(1,a+1) :
    a,b = map(int,input().split())
    print(f"Case #{i}: {a+b}")