# 2822번 : 점수 계산

score = []
idx = []
p = []
sum = 0

for i in range(8):
    a = int(input())
    score.append(a)
    
ss = sorted(score, reverse = True)

for i in range(5):
    sum += ss[i]
    idx.append(ss[i])
print(sum)
# print(idx)


for i in range(5):
    p.append(score.index(idx[i])+1)
p.sort()
print(*p)