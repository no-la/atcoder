N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

C = list(map(int, input().split()))

# 全方位木DP
sum_c = [0] * N
sum_d = [0] * N
# sum_c[i]: 頂点iの部分木の頂点xについてC[x]の総和
# sum_d[i]: 頂点iの部分木の頂点xについてC[x]*d(i, x)の総和

from collections import deque

todo = deque([(0,)])
seen = [False] * N  # ここはsetでもよい
seen[0] = True
while todo:
    v, *others = todo.pop()
    if v == -1:  # DFSの戻るときの処理
        v, w = others
        sum_c[v] += sum_c[w]
        sum_d[v] += sum_c[w] + sum_d[w]  # C[x]*(d(i, x) + 1) を足す
        continue

    # 頂点vの部分木における頂点vの寄与分を入れて置く
    sum_c[v] = C[v]
    sum_d[v] = 0

    for w in E[v]:
        if seen[w]:  # 既に調べた点は飛ばす
            continue
        seen[w] = True
        todo.append((-1, v, w))
        todo.append((w,))


# print(sum_c, sum_d, sep="\n")

f = [0] * N

# DFS
todo = deque([(0, 0, 0)])
seen = [False] * N
seen[0] = True
while todo:
    v, p_sum_c, p_sum_d = todo.pop()
    # v: 今の頂点
    # p_sum_c: vの部分木以外の頂点xについてC[x]の総和
    # p_sum_d: vの部分木以外の頂点xについてC[x]*d(i, x)の総和
    f[v] = sum_d[v] + p_sum_d
    for w in E[v]:
        if seen[w]:
            continue
        seen[w] = True
        # vの部分木におけるwの部分木の寄与分を減らして足す
        nx_sum_c = p_sum_c + sum_c[v] - sum_c[w]
        nx_sum_d = p_sum_d + sum_d[v] - (sum_d[w] + sum_c[w]) + nx_sum_c

        todo.append((w, nx_sum_c, nx_sum_d))

print(min(f))
