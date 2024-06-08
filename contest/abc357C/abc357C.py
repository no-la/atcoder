N = int(input())
M = 3**N

ans = [["-"]*M for _ in range(M)]

def f(i, j, k):
    if k==0:
        ans[i][j] = "#"
        return
    
    for si in range(0, 3):
        for sj in range(0, 3):
            if (si, sj)==(1, 1):
                for ni in range(3**(k-1)):
                    for nj in range(3**(k-1)):
                        ans[i+3**(k-1)+ni][j+3**(k-1)+nj] = "."
            else:
                f(i+si*(3**(k-1)), j+sj*(3**(k-1)), k-1)

f(0, 0, N)

for l in ans:
    print(*l, sep="")
