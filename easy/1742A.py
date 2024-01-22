# https://codeforces.com/problemset/problem/1742/A

for i in range(int(input())):
    lista = list(map(int, input().split()))
    lista = sorted(lista)

    if lista[2] == lista[0] + lista[1]:
        print("YES")
    else:
        print("NO")