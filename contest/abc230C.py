N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q+1):
    ans = []
    for j in range(R, S+1):
        if A-i==B-j or A-i==-B+j:
            ans.append("#")
        else:
            ans.append(".")
    print("".join(ans))