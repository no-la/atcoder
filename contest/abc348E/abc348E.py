N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    E[a].append(b)
    E[b].append(a)

C = list(map(int, input().split()))


# 各点に対して、その点から(1.葉に向かうとき 2.根に向かうとき)の以下の情報を用意する
# 葉(根)までのf(v)の和
# 葉(根)までのC[v]の和

