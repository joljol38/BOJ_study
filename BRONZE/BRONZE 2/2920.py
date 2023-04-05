m = list(map(int, input().split()))

a = sorted(m)
d = sorted(m, reverse = True)

if (a == m) :
    print("ascending")
elif (d == m) :
    print("descending")
else :
    print("mixed")