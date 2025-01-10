N = int(input())
S = input()

for i in range(1, N):
    ans = 0
    for l in range(N - i):
        if S[l] == S[l + i]:
            break
        ans = l + 1

    print(ans)
