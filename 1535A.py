# https://codeforces.com/problemset/problem/1535/A

for i in range(int(input())):
    s = list(map(int, input().split()))
    s1 = sorted(s[:2])
    s2 = sorted(s[2:])
    
    if s1[0] > s2[1] or  s2[0] > s1[1]:
        print("NO")
    else:
        print('YES')
