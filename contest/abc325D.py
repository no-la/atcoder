from heapq import heapify, heappop, heappush

N = int(input())
D = []
for i in range(N):
    t, d = map(int, input().split())
    D.append((t, d+t))
D.sort()

ans = 0
now = 0
i = 0 #商品のindex 1ずつ増やしていく
hq = [] #範囲内にある各商品が範囲外に出る時間を入れる
heapify(hq)
#nowをいい感じに増やしていく
while i<N:
    #now時に範囲内に入ったものが範囲外に出る時間をhqに追加
    while i<N and D[i][0]==now:
        heappush(hq, D[i][1])
        i += 1
    #既に過ぎたものをhqから取り出す
    while hq and now>hq[0]:
        heappop(hq)
    #次の商品が範囲内に入ってくるまで、期限の短い順に印字していく
    while hq and (i>=N or now<D[i][0]):
        t = heappop(hq)
        if now<=t:
            ans += 1
            now += 1 #1秒のインターバル
    #範囲内に商品がないときは時間を次の商品が来るところまで飛ばす
    if not hq and i<N:
        now = D[i][0]
        
print(ans)