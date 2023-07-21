# https://codeforces.com/contest/1850/problem/C

for i in range(int(input())):
    text = ''
    output = ''
    for i in range(8):
        a = input()
        text += a
    for k in text:
        if k.isalpha():
            output += k
    print(output)
