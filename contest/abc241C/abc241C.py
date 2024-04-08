N = int(input())
S = [input() for _ in range(N)]

# 全探索
# O(N^2 * 24) = O(2.4*10^7)
for i in range(N):
    for j in range(N):
        for h, w in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            cb = 0
            ni, nj = i, j
            for _ in range(6):
                if not(0<=ni<N and 0<=nj<N):
                    break
                cb += S[ni][nj]=="#"
                ni += h
                nj += w
            else:
                if cb>=4:
                    print("Yes")
                    exit()
print("No")