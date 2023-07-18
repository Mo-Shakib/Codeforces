# https://codeforces.com/problemset/problem/1542/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    

    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    if even == odd:
        print("Yes")
    else:
        print("No")