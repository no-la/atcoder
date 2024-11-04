from collections import deque

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        # DFS

        # todo: 次の点に進むクエリ(i>=0)と、指定した点をseenから取り除くクエリ(i<0)を入れる
        todo = deque([(i, j)])
        seen = set()  # 既に通り過ぎた点を入れる
        while todo:
            vi, vj = todo.pop()

            if vi < 0:  # 戻る時の処理
                seen.remove((-vi - 1, -vj))  # viについてはoffset分の-1を忘れずに
                continue

            # 次の点に進む
            seen.add((vi, vj))
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                wi, wj = vi + di, vj + dj
                if not (0 <= wi < H and 0 <= wj < W):
                    continue
                if S[wi][wj] == "#":
                    continue
                if (wi, wj) in seen:
                    continue

                if len(seen) == K:
                    ans += 1
                    continue
                # 戻る時の処理のクエリ
                # vi<0になるように-1しておく
                todo.append((-wi - 1, -wj))
                # 次の点に進むクエリ
                todo.append((wi, wj))

print(ans)
