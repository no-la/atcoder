N, M = map(int, input().split())
S = input()

for i in range(N+1):
    muji = M
    logo = i
    for j in range(N):
        if S[j]=="0":
            muji = M
            logo = i
        elif S[j]=="1":
            if muji>0:
                muji -= 1
            else:
                logo -= 1
        elif S[j]=="2":
            logo -= 1
        if muji<0 or logo<0:
            break
    else:
        break
print(i)