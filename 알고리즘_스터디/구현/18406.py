# 18406번 : 럭키 스트레이트 
N = input()
H = N[:len(N)//2]
T = N[len(N)//2:]
# print(H)
# print(T)
sum_h = 0
sum_t = 0
for i in range(len(H)):
    sum_h += int(H[i])
# print(sum_h)
for j in range(len(T)):
    sum_t += int(T[j])
# print(sum_t)

if (sum_h == sum_t) :
    print("LUCKY")
else :
    print("READY")