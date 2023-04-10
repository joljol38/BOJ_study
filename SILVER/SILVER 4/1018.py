# 1018번 : 체스판 다시 칠하기

N, M = map(int, input().split())
chess = []
result = []
for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        c1 = 0
        c2 = 0
        
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if chess[k][l] != "W":
                        c1 += 1
                    if chess[k][l] != "B":
                        c2 += 1
                else :
                    if chess[k][l] != "B":
                        c1 += 1
                    if chess[k][l] != "W":
                        c2 += 1
        result.append(c1)
        result.append(c2)

print(min(result))     