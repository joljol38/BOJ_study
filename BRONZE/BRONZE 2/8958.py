# 8958 : OX 퀴즈
a = int(input())

for i in range(a):
    score = 0
    total_score = 0
    b = input()
    
    for j in b:
        if j == 'O':
            score += 1
        else:
            score = 0
        total_score += score

    print(total_score)