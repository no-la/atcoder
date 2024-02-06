N = int(input())
data = {}
for i in range(N):
    k, v = map(int, input().split())
    data[k] = v
keys = sorted(data.keys())
ans = 0
for s in keys:
    #次のサイズ
    n = s*2
    #スライムの個数
    v = data[s]
    #できるだけ合体する
    while(v>0):
        if n not in data:
            ans += v%2
            v //= 2
            n *= 2
            # print(keys)
        else: #既に存在するサイズになるので、個数を足してbreak
            ans += v%2
            data[n] += v//2
            break
print(ans)