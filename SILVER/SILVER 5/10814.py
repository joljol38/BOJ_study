# 10814번 : 나이순 정렬

N = int(input())
member = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member.append((age, name))
    
member.sort(key = lambda x : x[0])

for x, y in member:
    print(x, y)
    