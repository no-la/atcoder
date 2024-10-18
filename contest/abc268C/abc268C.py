N = int(input())
P = list(map(int, input().split()))

P = P + P
temp = 0
for i in range(N):
    temp += P[i] == (P[i] - 1) % N or P[i] == (P[i]) % N or P[i] == (P[i] + 1) % N

ans = temp
for i in range(1, N):
    temp -= (
        P[i - 1] == (P[i - 1] - 1) % N
        or P[i - 1] == (P[i - 1]) % N
        or P[i - 1] == (P[i - 1] + 1) % N
    )
    temp += (
        P[i + N] == (P[i + N] - 1) % N
        or P[i + N] == (P[i + N]) % N
        or P[i + N] == (P[i + N] + 1) % N
    )
    ans = max(ans, temp)
    print(temp, P[i : i + N])


print(ans)
