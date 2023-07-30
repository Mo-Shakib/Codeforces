# https://codeforces.com/problemset/problem/520/A

t = int(input())
s = input().lower()
if len(set(s)) == 26:
    print("YES")
else:
    for i in range(97, 123):
        if chr(i) not in s:
            print("NO")
            break
