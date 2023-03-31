# 2675번 : 문자열 반복

a = int(input())

for i in range(a):
    b, s = input().split()
    
    for j in range(len(s)):
        
        print(s[j]*int(b), end ="")
    print("")