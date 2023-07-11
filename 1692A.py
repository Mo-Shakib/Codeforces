# https://codeforces.com/problemset/problem/1692/A

for i in range(int(input())):
    lst = list(map(int, input().split()))

    n = 0
    for i in range(1, len(lst)):
        if lst[0] < lst[i]:
            n += 1
    print(n)
        