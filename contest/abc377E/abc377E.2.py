N, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))


def apply_permutation(P, K):
    # 長さを取得
    n = len(P)

    # ダブリングテーブルの準備
    # doubling[i][j] は、2^i 回の置換を施したときの位置を示します
    doubling = [[0] * n for _ in range(61)]

    # 初期値を設定
    for i in range(n):
        doubling[0][i] = P[i]

    # ダブリングテーブルを構築
    for i in range(1, 61):
        for j in range(n):
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

    # 初期位置
    result = list(range(n))

    # K回施す
    for i in range(60):
        if (K >> i) & 1:  # K の i ビット目が立っている場合
            result = [doubling[i][x] for x in result]

    return result


print([v + 1 for v in apply_permutation(P, K)])
