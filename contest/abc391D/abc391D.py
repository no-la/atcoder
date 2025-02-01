N, W = map(int, input().split())
block_at = [[] for _ in range(W)]
blocks = []
for i in range(N):
    x, y = map(lambda x: int(x) - 1, input().split())
    block_at[x].append((y, i))

id_to_row = [0] * N
# id_to_row[i]: i個目のブロックが、その列の下から何個目か

for x in range(W):
    block_at[x].sort()
    for j, b in enumerate(block_at[x]):
        y, i = b
        blocks.append((y, x, j))
        id_to_row[i] = j + 1

blocks.sort()


vanish_times = [0]
# vanish_times[i]: i行消えるまでの時間
now = 0
ready = [0] * N
# ready[i]: 下からi+1個目のブロックのうちの消える準備ができているものの個数
target_row = 0
for i, b in enumerate(blocks):
    y, x, j = b
    ready[j] += 1
    now = y

    while target_row < N and ready[target_row] == W:
        now += 1
        vanish_times.append(now)
        target_row += 1


# 以下、クエリをこなす


Q = int(input())
for _ in range(Q):
    t, a = map(int, input().split())
    a -= 1
    i = id_to_row[a]
    print("Yes" if i >= len(vanish_times) or t < vanish_times[i] else "No")
    # print(i, len(vanish_times), t, (vanish_times[i] if i < len(vanish_times) else None))


# print(vanish_times)
# print(id_to_row)
