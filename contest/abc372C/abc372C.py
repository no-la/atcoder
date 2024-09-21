N, Q = map(int, input().split())
S = list(input())

l = ["A", "B", "C"]

ans = 0
for i in range(N - 2):
    ans += S[i : i + 3] == l


for _ in range(Q):
    x, c = input().split()
    x = int(x) - 1

    for i in range(3):
        if x + i - 2 < 0 or N < x + i + 1:
            continue
        if S[x + i - 2 : x + i + 1] == l:
            ans -= 1
            break

    S[x] = c
    for i in range(3):
        if x + i - 2 < 0 or N < x + i + 1:
            continue
        if S[x + i - 2 : x + i + 1] == l:
            ans += 1
            break
    print(ans)
