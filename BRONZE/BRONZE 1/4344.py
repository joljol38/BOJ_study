# 4344번 : 평균은 넘겠지
a = int(input())

for i in range(a):
    b = list(map(int, input().split()))
    c = sum(b[1:])/b[0]
    cnt = 0
    
    for j in b[1:]:
        if j > c:
            cnt += 1
    percentage = cnt/b[0] * 100
    print(f"{percentage:.3f}%")