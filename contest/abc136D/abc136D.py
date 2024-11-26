S = input()
N = len(S)

# ある程度繰り返すと RL に辿り着く
# あとは偶奇だけ気にする

ans = [0] * N
q = [0]
to = 0
for i in range(1, N):
    if S[i - 1] == S[i]:
        if S[i] == "R":  # RR
            q.append(i)
        else:  # LL
            ans[to + (i - to) % 2] += 1
    else:
        if S[i] == "R":  # LR
            q.append(i)
        else:  # RL
            ans[i] += 1
            while q:
                ans[i - 1 + (i - q.pop() + 1) % 2] += 1
            to = i - 1


print(*ans)
