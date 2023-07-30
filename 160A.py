# https://codeforces.com/problemset/problem/160/A

t = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
needToTake = sum(a) // 2

for i in range(1, t+1):
    if sum(a[:i]) > needToTake:
        print(i)
        break
