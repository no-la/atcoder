A, B, C, D = map(int, input().split())

unit = [[2, 1], [1, 2], [0, 1], [1, 0]]


ans = 0
for _ in range(4):
    if A==C:
        break
    ans += (unit[A%4][B%2]*(1+(D-B-1)//2) + unit[A%4][(B+1)%2]*((D-B)//2))*(1+(C-A-1)//4)
    A += 1

print(ans)
