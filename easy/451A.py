# https://codeforces.com/problemset/problem/451/A

m, n = map(int, input().split())

if min(m, n) % 2 == 0:
    print("Malvika")
else:
    print("Akshat")