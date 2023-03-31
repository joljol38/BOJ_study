# 2839번 : 설탕 배달
a = int(input())
count = 0

while a >= 0:
    if a % 5 == 0 : # 큰 수인 5로 나눈 나머지를 기준
        count += (a //5)
        print(count)
        break
    a -= 3
    count += 1
else :
    print(-1)
    