# https://codeforces.com/problemset/problem/131/A

s = input()

if s.isupper():
    print(s.lower())
elif s[0].islower() and len(s) == 1:
    print(s.upper())
elif s[0].islower() and s[1:].isupper():
    print(s[0].upper() + s[1:].lower())
else:
    print(s)