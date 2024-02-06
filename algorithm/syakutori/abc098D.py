#https://atcoder.jp/contests/abc098/submissions/49588780
N = int(input())
A = list(map(int, input().split()))

#尺取り法
ans = 0
right = 0
temp = 0
for left in range(N):
    while right<N and temp^A[right]==temp+A[right]: #条件の判定
        temp ^= A[right] #tempはint型になるので、^も+もうまく動いてくれる
        right += 1
    ans += right-left
    if left == right: #[left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else: #このあとleftを+1するので、その分の情報を削る
        temp ^= A[left] #xorの逆演算はxor
print(ans)