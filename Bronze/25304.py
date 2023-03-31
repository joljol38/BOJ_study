# 25304번 : 영수증

X = int(input())
N = int(input())
l = []
for i in range(1,N+1) :
    a,b = map(int, input().split())
    l.append(a*b)

if(sum(l) == X) :
    print("Yes")
else :
    print("No")