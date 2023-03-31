# 2941번 : 크로아티아 알파벳

s = input()
count = 0
t = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in t :
    if i in s :
        count += 1
# print(count)
# print(len(t))
new_s = s
for i in range (len(t)) :
    # print(t[i])
    # s.strip(t[i])
    new_s = new_s.replace(t[i], " ")
    # print(new_s)
    if " " in new_s :
        answer = len(new_s)
        # print(len(new_s))
    else : 
        answer = count + len(new_s.replace(" ",""))
        # print(count + len(new_s.replace(" ","")))
print(answer)
# print(len(new_s.replace(" ","")))
# print(count+len(new_s.replace(" ","")))
    