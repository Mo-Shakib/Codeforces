# https://codeforces.com/contest/1850/problem/D

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    count = []
    temp = 1  
    for j in range(1, n): 
        if a[j] - a[j-1] <= k:
            temp += 1
        else:
            count.append(temp)
            temp = 1
    count.append(temp)
    print(n - max(count))



    


