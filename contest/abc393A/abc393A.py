import sys

input = lambda: sys.stdin.readline().rstrip()
S, T = input().split()
if S == "sick" and T == "fine":
    print(2)
elif S == "sick" and T == "sick":
    print(1)
elif T == "fine":
    print(4)
else:
    print(3)
