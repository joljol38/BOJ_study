N = int(input())
x = 0
for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        x = i                   
        break

print(x)