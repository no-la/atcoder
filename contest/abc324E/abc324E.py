N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

front = [0]*N
back = [0]*N
# front[i]: S[i]の部分文字列であり、Tの先頭から始まる連続部分文字列と一致する長さの最大値
# backも同様
for i in range(N):
    j = 0
    for s in S[i]:
        if s==T[j]:
            front[i] += 1
            j += 1
        
        if j>=len(T):
            break
    

for i in range(N):
    j = 0
    for s in S[i][::-1]:
        if s==T[len(T)-1-j]:
            back[i] += 1
            j += 1
        
        if j>=len(T):
            break

# print(front)
# print(back)
back.sort()

import bisect
# 基本的にbisect_leftを使う
# 渡す配列は昇順(reverse=False)ソートしておく
ans = 0
for f in front:
    ans += N - bisect.bisect_left(back, len(T)-f)

print(ans)
