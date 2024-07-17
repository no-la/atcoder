N = int(input())
S = input()
MOD = 998244353
M = 10

def index(s):
    return ord(s)-ord("A")

# bitDPぽい感じ
dp = [[[0]*M for _ in range(2**M)] for _ in range(N)]
# dp[i][j][k]: S[:i+1]まででjで表されるコンテストに出場し、最後はkである場合の数
