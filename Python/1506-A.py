# https://codeforces.com/contest/1506/problem/A
# n = row, m = collum
t = int(input())
for i in range(t):
    n, m, x = map(int, input().split())
    lenth = n*m
    arr = []
    a = 1
    for j in range(m):
        arr.append(a)
        a += n 
print(arr)

