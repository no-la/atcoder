N = int(input())
S = input()
C = list(map(int, input().split()))

dpl = [[0]*N for _ in range(2)] # dpl[i][j]: [0, j]が互いに異なり、[j]がiになるための最小コスト
dpr = [[0]*N for _ in range(2)] # dpr[i][j]: [-j, -1]が互いに異なり、[-j]がiになるための最小コスト
dpl[(int(S[0])+1)%2][0] +=C[0]
dpr[(int(S[-1])+1)%2][0] += C[-1]
for j in range(1, N):
    for i in range(2):
        ii = (i+1)%2
        dpl[i][j] = dpl[ii][j-1] + (C[j] if (S[j]!=str(i)) else 0)
        dpr[i][j] = dpr[ii][j-1] + (C[-j-1] if S[-j-1]!=str(i) else 0)


ans = 10**15
for j in range(N-1):
    ans = min(
        ans,
        min([dpl[i][j] + dpr[i][N-j-2] for i in range(2)])
        )
print(ans)