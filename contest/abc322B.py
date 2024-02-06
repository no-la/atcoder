N, M = map(int, input().split())
S = input()
T = input()

if T[:N] == S:
    if T[-N:] == S:
        ans = 0
    else:
        ans = 1
else:
    if T[-N:] == S:
        ans = 2
    else:
        ans = 3

print(ans)
