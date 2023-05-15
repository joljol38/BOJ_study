A = input().split("-")
num = []
for i in A:
    cnt = 0
    sum = i.split('+')
    for j in sum:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)