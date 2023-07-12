# https://codeforces.com/contest/1660/problem/A

for i in range(int(input())):
    ones, twos = map(int, input().split())
    if ones == 0:
        print(1)
    else:
        print(ones+twos+twos+1)