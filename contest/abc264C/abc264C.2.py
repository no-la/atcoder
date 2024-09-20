H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

# bit全探索
N = H1 + W1
for i in range(2**N):
    h_tar, w_tar = [], []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        if j < H1:
            h_tar.append(j)
        else:
            w_tar.append(j - H1)
    if len(h_tar) == H2 and len(w_tar) == W2:
        is_same = True
        for h in range(H2):
            for w in range(W2):
                if A[h_tar[h]][w_tar[w]] != B[h][w]:
                    is_same = False
        if is_same:
            print("Yes")
            exit()

print("No")
