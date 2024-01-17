# https://codeforces.com/contest/1296/problem/A

for i in range(int(input())):
    x = int(input())
    lista = list(map(int, input().split()))

    if sum(lista) % 2 == 0:
        print('NO')
    else:
        print('YES')