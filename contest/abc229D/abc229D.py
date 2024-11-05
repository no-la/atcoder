S = input()
K = int(input())
N = len(S)

# .がK個以下である最大の区間

# 尺取り法
ans = 0
right = 0
count = 0
for left in range(N):
    while right < N and count + (S[right] == ".") <= K:
        count += S[right] == "."
        right += 1
    ans = max(ans, right - left)
    if left == right:  # [left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else:  # このあとleftを+1するので、その分の情報を削る
        count -= S[left] == "."

print(ans)
