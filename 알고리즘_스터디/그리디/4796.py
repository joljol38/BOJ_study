# 4796번 : 캠핑

count = 1
while True :
    L, P, V = map(int, input().split())
    if (L == 0 and P == 0 and V == 0) :
        break
    n = (V % P)
    if L < n: # L이 나머지 보다 작은 예외사항
        n = L
        
    answer = (V//P) * L + n
    print(f"Case {count}: {answer}")
    count += 1