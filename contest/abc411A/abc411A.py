import sys

input = lambda: sys.stdin.readline().rstrip()
P = input()
L = int(input())

print("Yes" if len(P) >= L else "No")
