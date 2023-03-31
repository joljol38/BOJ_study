# 10988번 : 팰린드롬인지 확인하
s = input()
if (len(s) % 2) == 0 :
    half = s[(len(s) // 2) : len(s) + 1]
    if s[0 : (len(s) // 2)] == (half[::-1]) :
        print(1)
    else :
        print(0)
elif (len(s) % 2) == 1 :
    half = s[(len(s) // 2)+1 :]
    if s[:(len(s) // 2)] == (half[::-1]) :
        print(1)
    else : 
        print(0)