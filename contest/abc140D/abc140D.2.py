N, K = map(int, input().split())
S = input()+"*"

# LのあつまりとRのあつまり、多い方を反転させる
now = S[0]
count = {"L":0, "R":0}
i = 1
while i<len(S):
    if S[i]==now:
        i += 1
    else:
        count[now] += 1
        now = S[i]
        i += 1

ans = 0
tar = "L" if count["L"]<count["R"] else "R"
remain = K
start = False
# print(count, tar)
for i in range(1, len(S)):
    if not start and S[i-1]!=S[i]:
        start = True
        continue
    if S[i-1]==S[i]:
        ans += 1
    elif remain>0 and S[i-1]==tar and i+1<len(S):
        ans += 2
        remain -= 1


if remain>0 and S[0]=="L":
    ans += 1
    remain -= 1
if remain>0 and S[-2]=="R":
    ans += 1
    remain -= 1

print(min(ans, N-1))

    