N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


# Xより大きいもの、Yより小さいものを含まない最大の部分列
# X, Yを含む最小の部分列
# の2つを調べる


# Xより大きいもの、Yより小さいものを含まない最大の部分列
# ごとに調べればいい

d = [i for i in range(N) if A[i]>X or A[i]<Y] # 条件を満たさない点
d.append(N)
# print(d)
# 尺取り法
ans = 0
right = 0
has_X, has_Y = 0, 0
ll = -1
for rr in d:
    # print("rr", rr)
    for left in range(ll+1, rr):
        while right<rr and (not has_X or not has_Y):
            if A[right]==X:
                has_X += 1
            if A[right]==Y:
                has_Y += 1

            right += 1
            
        if has_X and has_Y:
            # print((ll, rr), (left, right), (has_X, has_Y))
            ans += rr-(right-1)
            
        if left == right: # [left, right)が空集合なので'temp=初期値'になっているはず
            right += 1
        else: #このあとleftを+1するので、その分の情報を削る
            if A[left]==X:
                has_X -= 1
                # print("del X")
            if A[left]==Y:
                has_Y -= 1
                # print("del Y")
    ll = rr
            
            

print(ans)
