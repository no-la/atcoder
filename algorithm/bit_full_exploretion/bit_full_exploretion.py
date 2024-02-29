
# bit全探索
A = []
N = len(A)
for i in range(2 ** N):
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        # A[j]を選ぶ場合なので、適当な処理を書く