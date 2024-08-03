N = int(input())
A = list(map(int, input().split()))

ans = 0

for bit in range(30):
    count = [0] * 2  # 0のカウントと1のカウントを保持する
    total = 0
    
    for i in range(N):
        count[(A[i] >> bit) & 1] += 1
        total += count[~((A[i] >> bit) & 1) & 1]
    
    ans += total * (1 << bit)

print(ans)

