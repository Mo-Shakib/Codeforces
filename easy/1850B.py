# https://codeforces.com/contest/1850/problem/B

def sol(d):
    sorted_d = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
    for key, value in sorted_d:
        if value[0] <= 10:
            return key + 1



for i in range(int(input())):
    count = 0
    d = {}
    b_values = []
    for j in range(int(input())):
        a, b = map(int, input().split())
        b_values.append(b)
        d[count] = [a, b]
        count += 1
    print(sol(d))



