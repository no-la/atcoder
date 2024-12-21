H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
T = input()

now = [X - 1, Y - 1]
ans = set()
if S[now[0]][now[1]] == "@":
    ans.add(tuple(now))
for i, t in enumerate(T):
    s = t
    if s == "L":
        delta = (0, -1)
    elif s == "R":
        delta = (0, 1)
    elif s == "U":
        delta = (-1, 0)
    elif s == "D":
        delta = (1, 0)

    nnow = [now[0] + delta[0], now[1] + delta[1]]
    if not (0 <= nnow[0] < H and 0 <= nnow[1] < W):
        continue
    if S[nnow[0]][nnow[1]] == "#":
        continue
    now = nnow
    if S[now[0]][now[1]] == "@":
        ans.add(tuple(now))

# print(ans)
print(*[v + 1 for v in now], len(ans))
