N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
D = [None,2,5,5,4,5,6,3,7,6] # D[i]: 数字iを作るために必要なマッチの数

# 桁の大きい方から見ていってその時作れる最大の数字を作る
count = 0
ans = []
while True:
    for a in A:
        if count+D[a]<=count:
            count += D[a]
            ans.append(a)
            break
    else:
        break

print(sum([10**i*a for i, a in enumerate(ans)]))