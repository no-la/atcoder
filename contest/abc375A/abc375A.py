N = int(input())
S = input()

ans = 0
for i in range(N - 2):
    ans += S[i] == S[i + 2] == "#" and S[i + 1] == "."

print(ans)
