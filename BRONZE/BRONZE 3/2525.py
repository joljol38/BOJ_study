# 2525번 : 오븐 시계

a, b = map(int, input().split())
c = int(input())

h = (a*60 + b + c) // 60
m = (a*60 + b + c) % 60

if (h >= 24) :
    print(h-24,m)
else : 
    print(h,m)
