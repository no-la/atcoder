N = int(input())
S = [0] + list(map(int, input().split()))

ans = [S[i] - S[i - 1] for i in range(1, N + 1)]
print(*ans)
