H, W = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

def check(tar):
    for h in range(H):
        for w in range(W):
            if A[tar[0][h]][tar[1][w]]!=B[h][w]:
                return False
    return True

def to_string(tar):
    val = "".join(map(str, tar[0]))
    val += "".join(map(str, tar[1]))
    return val

def get_next_target(is_horizontal, tar_id, tar_list):
    import copy
    w = copy.deepcopy(tar_list)
    temp = w[is_horizontal][tar_id+1]
    w[is_horizontal][tar_id+1] = w[is_horizontal][tar_id]
    w[is_horizontal][tar_id] = temp
    w[2] += 1
    return w
    

todo = [[[i for i in range(H)],[i for i in range(W)], 0]] #[行の順番, 列の順番, 回数]
seen = set()
ans = 10000000000 if not check(todo[0]) else 0
seen.add(to_string(todo[0]))
while todo: #回数の小さい方から調べるのでBFS
    v = todo.pop(0)
    for n in range(2):
        for i in range([H-1, W-1][n]):
            w = get_next_target(n, i, v)
            w_str = to_string(w)
            if w_str not in seen:
                seen.add(w_str)
                todo.append(w)
                b = check(w)
                if b:
                    ans = min(ans, w[2])

ans = -1 if ans==10000000000 else ans
print(ans)
