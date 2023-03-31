# 10809 : 알파벳 찾기
a = input()

list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(26):
    if a.find(list[i]) != -1 :
        list[i] = a.find(list[i])
    else :
        list[i] = -1
print(list)