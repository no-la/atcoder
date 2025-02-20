import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 数えながら尺取り
# 尺取り法
ans = 1
right = 0
temp = defaultdict(int)
count = 0
for left in range(N):
    while right < N and count <= K:
        temp[A[right]] += 1
        if temp[A[right]] == 1:
            count += 1

        right += 1
    # print(left, right, temp)
    if right == N and count <= K:
        ans = max(ans, N - left)
    else:
        ans = max(ans, right - 1 - left)

    if left == right:  # [left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else:  # このあとleftを+1するので、その分の情報を削る
        temp[A[left]] -= 1
        if temp[A[left]] == 0:
            count -= 1

print(ans)
