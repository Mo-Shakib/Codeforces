# https://codeforces.com/problemset/problem/116/A

current = 0

for i in range(int(input())):
    
    a, b = map(int, input().split())
    
    if i == 0:
        max = b
        current = b
    else:
        current = current - a + b
        if current > max:
            max = current

print(max)