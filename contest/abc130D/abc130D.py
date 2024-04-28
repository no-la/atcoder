N, K = map(int, input().split())
A = list(map(int, input().split()))


# 尺取り法
d = []
right = 0
temp = 0 #部分列による値（条件の判定に必要なときに使う）
for left in range(N):
    while temp<K and right<N: # 条件の判定
        temp += A[right]
        right += 1
    if temp>=K:
        d.append((left, right))
    else:
        pass
    if left == right: # [left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else: #このあとleftを+1するので、その分の情報を削る
        temp -= A[left]

# print(*d, sep="\n")

ans = 0
for l, r in d:
    ans += N-r+1

print(ans)
