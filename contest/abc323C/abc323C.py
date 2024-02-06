N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for i in range(N)]

#現在の点数
scores = [i+1 for i in range(N)]
#まだ解いていない問題の点数
remain = [[] for i in range(N)]
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            scores[i] += A[j]
        else:
            remain[i].append(A[j])
    remain[i].sort(reverse=True)

#各iについて調べていく
for i in range(N):
    sup = max(scores)
    v = scores[i]
    if sup==v:
        if scores.count(scores[i]) != 1:
            print(1)
            continue
        else:
            print(0)
            continue
    else:
        for j in range(M):
            v += remain[i][j]
            if v>sup:
                print(j+1)
                break
            