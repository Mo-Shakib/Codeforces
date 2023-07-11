# https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
puzzels = list(map(int, input().split()))

puzzels.sort()
min_diff = 1000
for i in range(m-n+1):
    diff = puzzels[i+n-1] - puzzels[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)