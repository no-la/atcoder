S = input()
T = input()
N = len(S)
M = len(T)

dp_front = [False] * (M + 1)
dp_back = [False] * (M + 1)
# dp_front[i]: S[:i]==T[:i]
# dp_back[i]: S[-i:]==T[-i:]
dp_front[0] = True
dp_back[0] = True

for i in range(M):
    dp_front[i + 1] = dp_front[i] and (S[i] == T[i] or S[i] == "?" or T[i] == "?")
    dp_back[i + 1] = dp_back[i] and (
        S[-i - 1] == T[-i - 1] or S[-i - 1] == "?" or T[-i - 1] == "?"
    )

for x in range(M + 1):
    print("Yes" if dp_front[x] and dp_back[M - x] else "No")
