N = int(input())
S = [input() for _ in range(N)]

data_line = [set() for _ in range(N)]
data_row = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j]=="o":
            data_line[i].add(j)
            data_row[j].add(i)

ans = 0
for i in range(N):
    l = len(data_line[i])
    if l<2:
        continue
    for j in data_line[i]:
        k = len(data_row[j])
        if k>=2:
            ans += (l-1)*(k-1)
print(ans)            