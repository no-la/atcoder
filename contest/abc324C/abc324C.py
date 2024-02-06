N, T = input().split()
N = int(N)

ans = []
for i in range(N):
    S = input()
    id = i+1
    k, l = len(T), len(S)
    ok = False
    if k == l-1: #SがTに一文字を追加して得られるかどうかを判定する
        b = True
        for j in range(l):
            if b:
                if j < k and S[j] == T[j]:
                    continue
                else:
                    b = False
            elif S[j] != T[j-1]:
                break
        else:
            ok = True
    elif k == l+1: #SがTの1文字を消して得られるかどうか
        b = True
        for j in range(k):
            if b:
                if j < l and S[j] == T[j]:
                    continue
                else:
                    b = False
            elif S[j-1] != T[j]:
                break
        else:
            ok = True
    elif k == l: #SがTの1文字を変更して得られるかどうか
        b = True
        for j in range(k):
            if b:
                if S[j] == T[j]:
                    continue
                else:
                    b = False
            elif S[j] != T[j]:
                break
        else:
            ok = True

    if ok:
        ans.append(id)
ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))