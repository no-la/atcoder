N = int(input())


for i in range(10**6, 0, -1):
    if i**3>N:
        continue
    # 回文か判定する
    s = str(i**3)
    n = len(s)
    if n%2==0 and s[:n//2]==s[n-1:n//2-1:-1]:
        print(s)
        break
    elif n%2==1 and s[:n//2]==s[n-1:n//2:-1]:
        print(s)
        break