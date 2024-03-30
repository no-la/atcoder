N, A, B = map(int, input().split())
D = list(map(int, input().split()))

MOD = A+B
left = 0
right = 0
for i in range(1, N):
    x = (D[i]-D[0])%MOD
    y = (D[0]-D[i])%MOD
    nl = min(left, -y)
    nr = max(right, x)
    if abs(left-nl)<abs(right-nr):
        left = nl
    else:
        right = nr

print("Yes" if right+abs(left)<A else "No")