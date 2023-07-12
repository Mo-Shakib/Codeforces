# https://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())
a = list(map(int, input().split()))

time = 0
current = 1
for i in range(m):
    if a[i] >= current:
        time += a[i] - current
    else:
        time += n - current + a[i]
    current = a[i]
print(time)
