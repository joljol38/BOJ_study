# 2439번 : 별 찍기 - 2
a = int(input())

for i in range(1,a+1) :
    print(str("*"*i).rjust(a))