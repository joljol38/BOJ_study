T = int(input())

for i in range(T):
   cal = list(map(str, input().split()))
   ans = 0
   for i in range(len(cal)):
        if i == 0:
           ans += float(cal[0])
        else:
            if cal[i] == "@":
               ans *= 3
            elif cal[i] == "%":
               ans += 5
            elif cal[i] == "#":
               ans -= 7
   print("%0.2f" % ans)