N, A, B = map(int, input().split())
S = input()


# Aを先に必要なだけやると考えてよい
# Aを選ぶ回数の全探索で、Bを何回使うか数える

ans = B * N
for i in range(N):
    temp = A * i
    T = S[i:] + S[:i]
    for j in range(N // 2):
        temp += B * (T[j] != T[-j - 1])
    ans = min(ans, temp)

print(ans)
