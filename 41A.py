# https://codeforces.com/problemset/problem/41/A

t = input()
s = input()

if t == s[::-1]:
    print("YES")
else:
    print("NO")