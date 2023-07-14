# https://codeforces.com/problemset/problem/1560/A

t = int(input())
for _ in range(t):
    k = int(input())
    n = 1
    while k > 0:
        if n % 3 != 0 and n % 10 != 3:
            k -= 1
        n += 1
    print(n - 1)