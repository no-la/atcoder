N = int(input())
H = list(map(int, input().split()))

wall = [0] # 残っている意味のある壁のid

ans = [0]*N
ans[0] = H[0]+1
for i in range(1, N):
    while wall and H[wall[-1]]<=H[i]:
        wall.pop()
    # print(wall)
    if wall:
        ans[i] = ans[wall[-1]] + H[i]*(i-wall[-1])
    else:
        ans[i] = H[i]*(i+1)+1
    wall.append(i)


print(*ans)

