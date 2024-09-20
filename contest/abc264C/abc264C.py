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
    a = A.copy()
    w_count = 0
    h_count = 0
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        if j < H:
            a = a[: j - h_count] + a[j - h_count + 1 :]
            h_count += 1
        else:
            hj = j - H - h_count
            for k in range(len(a)):
                a[k] = a[k][:hj] + a[k][hj + 1 :]
            h_count += 1
    if f(a):
        print("Yes")
        exit()

print("No")
