# 4153번 : 직각삼각형

while True:
    number = list(map(int, input().split()))
    
    if (number[0] and number[1] and number[2]) == 0 :
        break
    else :
        if ((number[0]**2) + (number[1]**2) == (number[2]**2)) or ((number[0]**2) + (number[2]**2) == (number[1]**2)) or ((number[1]**2) + (number[2]**2) == (number[0]**2)):
            print("right")
        else :
            print("wrong")