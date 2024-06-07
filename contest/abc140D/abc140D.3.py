N, K = map(int, input().split())
S = input()+"*"
if N==1:
    print(0)
    exit()

ans = 0
for tar in ["L", "R"]:
    temp = 0
    remain = K
    start = S[0]==tar
    # print(count, tar)
    for i in range(1, len(S)):
        if not start and S[i-1]!=S[i]:
            start = True
            continue
        if S[i-1]==S[i]:
            temp += 1
        elif remain>0 and S[i-1]==tar and S[i]!="*":
            temp += 2
            remain -= 1

    if remain>0 and S[0]=="L" and tar=="L":
        temp += 1
        remain -= 1
    if remain>0 and S[-2]=="R" and tar=="R":
        temp += 1
        remain -= 1
    
    ans = max(temp, ans)

print(min(ans, N-1))

    