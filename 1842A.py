# https://codeforces.com/problemset/problem/1842/A

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if sum(a) == sum(b):
        print('Draw')
    elif sum(a) > sum(b):
        print('Tsondu')
    else:
        print('Tenzing')