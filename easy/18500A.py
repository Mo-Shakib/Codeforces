# https://codeforces.com/contest/1850/problem/A

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    # Check if any two elements have a sum greater than or equal to 10
    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        print("YES")
    else:
        print("NO")
    
    
