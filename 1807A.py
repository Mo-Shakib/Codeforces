# https://codeforces.com/problemset/problem/1807/A

for i in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] + a[1] == a[2]:
        print('+')
    elif a[0] - a[1] == a[2]:
        print('-')