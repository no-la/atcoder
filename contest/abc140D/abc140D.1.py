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
now = S[0]
start = False
print(tar)
i = 0
while i<len(S)-1:
    i += 1
    if S[i]==now:
        ans += 1
    else:
        if not start:
            start = True
            now = S[i]
            continue
        if remain>0 and now==tar and i+1!=len(S):
            print("turn", i)
            ans += 2
        now = S[i]
        remain -= 1

if remain>0 and S[0]=="L":
    ans += 1
    remain -= 1
if remain>0 and S[-2]=="R":
    ans += 1
    remain -= 1

print(ans)

    