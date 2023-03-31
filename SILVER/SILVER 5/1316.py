# 1316번 : 그룹 단어 체커
N = int(input())
cnt = 0
for i in range(N):
    s = input()
    for j in range(len(s)-1):
        if s[j] == s[j+1] :
            pass
        elif s[j] in s[j+1:]:
            cnt += 1
            break
# print(cnt)
print(N-cnt)
