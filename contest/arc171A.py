T = int(input())
ans = []
for _ in range(T):
    N, A, B = map(int, input().split())
    n2 = (N+1)/2 if N&1 else N/2
    temp = None
    if A>N or B>n2*N:
        temp = "No"
    elif A>=n2:
        v = (N-A)**2  #ポーンを置けるマス
        if B<=v:
            temp = "Yes"
        else:
            temp = "No"
    else:
        v = (N-A)*n2
        if B<=v:
            temp = "Yes"
        else:
            temp = "No"
    ans.append(temp)
print("\n".join(ans))