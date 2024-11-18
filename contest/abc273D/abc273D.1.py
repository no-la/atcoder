from collections import defaultdict

H, W, *pos = map(int, input().split())
N = int(input())
columns = defaultdict(list)
rows = defaultdict(list)
for _ in range(N):
    r, c = map(int, input().split())
    columns[r].append(c)
    rows[c].append(r)
Q = int(input())

# ソート
for k in columns:
    columns[k].sort()
for k in rows:
    rows[k].sort()

# 二分探索で一番近い壁を探せばいい
import bisect

# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    if d == "L":
        i, j = 0, 1
        tar = columns[pos[i]]
        from_ = pos[j]
        nearest_wall_id = bisect.bisect_left(tar, from_) - 1
        to = max(1, from_ - l)
        if nearest_wall_id < 0 or tar[nearest_wall_id] < to:
            pos[j] = to
        else:
            pos[j] = tar[nearest_wall_id] + 1
    elif d == "R":
        i, j = 0, 1
        tar = columns[pos[i]]
        from_ = pos[j]
        nearest_wall_id = bisect.bisect_left(tar, from_)
        to = min(W, from_ + l)
        if nearest_wall_id >= len(tar) or to < tar[nearest_wall_id]:
            pos[j] = to
        else:
            pos[j] = tar[nearest_wall_id] - 1
    elif d == "U":
        i, j = 1, 0
        tar = rows[pos[i]]
        from_ = pos[j]
        nearest_wall_id = bisect.bisect_left(tar, from_) - 1
        to = max(1, from_ - l)
        if nearest_wall_id < 0 or tar[nearest_wall_id] < to:
            pos[j] = to
        else:
            pos[j] = tar[nearest_wall_id] + 1
    else:
        i, j = 1, 0
        tar = rows[pos[i]]
        from_ = pos[j]
        nearest_wall_id = bisect.bisect_left(tar, from_)
        to = min(H, from_ + l)
        if nearest_wall_id >= len(tar) or to < tar[nearest_wall_id]:
            pos[j] = to
        else:
            pos[j] = tar[nearest_wall_id] - 1

    # print(*pos, "wall=", tar[nearest_wall_id] if 0<=nearest_wall_id<len(tar) else '-', "tar=", tar)
    print(*pos)
