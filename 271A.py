# https://codeforces.com/problemset/problem/271/A

n = int(input())
# find the next year with distinct digits
while True:
    n += 1
    if len(set(str(n))) == 4:
        print(n)
        break
