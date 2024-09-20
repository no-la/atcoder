H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]


def f(changed_a):
    """if chagne_a is B or not"""
    if len(changed_a) != H2:
        return False
    if len(changed_a[0]) != W2:
        return False

    for h in range(H2):
        for w in range(W2):
            if changed_a[h][w] != B[h][w]:
                return False
    return True


# bit全探索
N = H + W
for i in range(2**N):
    h_tar = []
    w_tar = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        if j < H:
            h_tar.append(j)
        else:
            w_tar.append(j - H)
    h_tar.append(H + 1)
    w_tar.append(W + 1)

    a = []
    before_k = 0
    for k in h_tar:
        a.append(A[before_k:k])
        before_k = k + 1
    b = [[None] * (W - len(w_tar) + 1) for _ in range(len(a))]
    before_l = 0
    for l in w_tar:
        for hi in range(len(a)):
            b[hi] = a[before_l:l]
        before_l = l + 1
    # print(h_tar, w_tar, sep="\n")
    # print(b, sep="\n")
    if f(b):
        print("Yes")
        exit()

print("No")
