# https://codeforces.com/problemset/problem/25/A

n = int(input())
numbers = list(map(int, input().split()))
even = odd = 0
for i in range(n):
    if numbers[i] % 2 == 0:
        even += 1
        even_index = i
    else:
        odd += 1
        odd_index = i

print(even_index + 1 if even == 1 else odd_index + 1)