import itertools
N, H, W = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
HW = H*W

# 必要条件(タイルの合計面積==HW)で使うタイルの組を絞る
tiles_list = []
# bit全探索
for i in range(2 ** N):
    surface = 0
    temp = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        temp.append(T[j])
        surface += T[j][0]*T[j][1]
    if surface==HW:
        tiles_list.append(temp)

# len(tiles_list) < 2^N<2^7=128
# len(tiles_list[_]) < N<7
# tiles_list[_]の並び順 < N!<7!=5040
# tiles_list[_][0, 1]の入れ替え(裏表、回転) < 2^N<128

# tiles_listから、並び順と裏表、回転を考慮して全探索
# O(2^N * N! * 2^N) < 128*5040*128 ~ 8*10^7
for tiles in tiles_list:
    for l in itertools.permutations(tiles, len(tiles)): # 並び替えの全探索
        for i in range(2 ** N): # 裏表、回転の全探索
            surface = 0
            t = []
            for j in range(len(tiles)):
                t.append(l[j] if (i>>j)&1 else [l[j][1], l[j][0]])
            
            # tが置けるかを調べる
            # マスを左上から順に見て行って、空いているマスに次のタイルを置いていく
            # 置けなかったら次のループ
            # 全部置けたらYesで終わり
            M = [[0, 0] for _ in range(H)] # M[h]: h行目のすでにタイルが置かれている半開区間
            i = 0 # マスのid 
            n = 0 # 次に置くタイルのid
            while n<len(t):
                h, w = divmod(i, W)
                if M[h][0]<=w<M[h][1]: # 既に置かれてるとき
                    i = h*W + M[h][1] # iを進める
                    continue
                
                # (h, w)はまだ置かれていないマスなので、置けるか調べ、置けるなら置く
                if M[h][1]+t[n][0]<=W and h+t[n][1]<=H: # 置ける
                    for j in range(h, h+t[n][1]): # 置く
                        M[j][1] += t[n][0]
                    i += t[n][0]
                    n += 1
                else: # 置けない
                    break
            else:
                print("Yes")
                exit()
print("No")