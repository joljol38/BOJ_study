# 4673번 : 셀프 넘버 
def d(n):
    n = n + sum(map(int, str(n)))
    return n

no_selfnum = set()

for i in range(1,10001):
    no_selfnum.add(d(i))
    
for j in range(1, 10001):
    if j not in no_selfnum:
        print(j)