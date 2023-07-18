# https://codeforces.com/problemset/problem/584/A

n, t = map(int, input().split())


x = 10**(n-1)
y = 10**n - 1


next_multiple = ((x + t - 1) // t) * t

if next_multiple > y:
    print(-1)
else:
    print(next_multiple)
