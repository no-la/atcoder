N = int(input())
S = [input() for _ in range(N)]

j = 0
while True:
    ans = []
    last = -1
    for i in range(N):
        if j>=len(S[N-1-i]):
            ans.append("*")
        else:
            ans.append(S[N-1-i][j])
            last = i
    if last==-1:
        break
    print("".join(ans[:last+1]))
    j += 1
