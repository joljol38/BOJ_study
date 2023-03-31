# 2480번 : 주사위 세개

a, b, c = map(int, input().split())

if (a == b == c) :
    print(10000+(a*1000))
elif (a == b !=c) :
    print(1000 + a*100)
elif (a == c != b) :
    print(1000 + a*100)
    
elif (b == c != a) :
    print(1000 + b*100)
else :
    l = [a,b,c]
    print(max(l)*100)