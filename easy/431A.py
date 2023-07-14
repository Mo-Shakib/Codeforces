# https://codeforces.com/problemset/problem/431/A

def calculate_cost(a1: int, a2: int, a3: int, a4: int, s: str) -> int:
    count = 0
    for i in s:
        if i == '1':
            count += a1
        elif i == '2':
            count += a2
        elif i == '3':
            count += a3
        else:
            count += a4
    return count

a1, a2, a3, a4 = map(int, input().split())
s = input()
print(calculate_cost(a1, a2, a3, a4, s))

