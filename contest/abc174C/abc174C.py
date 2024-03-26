K = int(input())
# mod K で調べる
# 0が出る前にループしたら無い
seen = [False]*K
t = 7%K
c = 1
while not seen[t]:
    if t==0:
        print(c)
        exit()
    if seen[t]:
        break
    seen[t] = True
    t = (t*10 + 7)%K
    c += 1
print(-1)