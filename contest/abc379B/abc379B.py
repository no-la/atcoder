N, K = map(int, input().split())
S = input()
i = 0
ans = 0
while i < N:
    count = 0
    while i < N and S[i] == "O":
        i += 1
        count += 1
    ans += count // K
    i += 1

print(ans)
