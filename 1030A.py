# https://codeforces.com/problemset/problem/1030/A


def isEasy(lst):
    if '1' in lst:
        return "HARD"
    return "EASY"


t = int(input())
a = input().split()
print(isEasy(a))