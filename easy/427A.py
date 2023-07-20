# https://codeforces.com/problemset/problem/427/A
t = int(input())
ans = 0

a = list(map(int, input().split()))
police = 0
crime = 0

for i in range(len(a)):
    if a[i] > 0:
        police += a[i]
    else:
        if police < 1:
            crime += 1
        else:
            police -= 1
print(crime)
