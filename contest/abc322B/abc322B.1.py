N, M = map(int, input().split())
S = input()
T = input()

if S == T[:N]:
    if S == T[-N:]:
        print(0)
    else:
        print(1)
else:
    if S == T[-N:]:
        print(2)
    else:
        print(3)
