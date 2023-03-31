# 1157번 : 단어 공부

alphabet = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
    'E' : 0,
    'F' : 0,
    'G' : 0,
    'H' : 0,
    'I' : 0,
    'J' : 0,
    'K' : 0,
    'L' : 0,
    'M' : 0,
    'N' : 0,
    'O' : 0,
    'P' : 0,
    'Q' : 0,
    'R' : 0,
    'S' : 0,
    'T' : 0,
    'U' : 0,
    'V' : 0,
    'W' : 0,
    'X' : 0,
    'Y' : 0,
    'Z' : 0
} 

a = input()
s = a.upper()
for i in range(len(s)):
    alphabet[s[i]] += 1
    
max_key = [k for k,v in alphabet.items() if max(alphabet.values()) == v]

if (len(max_key) >= 2) :
    print("?")
elif (len(max_key) == 1) :
    print(*max_key)
