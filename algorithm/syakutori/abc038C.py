#https://atcoder.jp/contests/abc038/submissions/49588377
N = int(input())
A = list(map(int, input().split()))

#尺取り法
ans = 0
right = 0
for left in range(N):
    while right==left or (1<=right<N and A[right-1]<A[right]): #条件の判定
        right += 1
    ans += right-left
    if left == right: #[left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else: #このあと、leftを+1するので、その分の情報を削る
        pass

print(ans)