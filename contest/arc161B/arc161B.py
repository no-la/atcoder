T = int(input())
for _ in range(T):
    N = int(input())

    ans = 0
    count = 0
    i = N.bit_length()-1
    if N.bit_count()==1 or (N.bit_count()==2 and N&1):
        i -= 1
    for __ in range(3):
        while i>=0:
            if ans+(1<<i)<=N:
                ans += 1<<i
                count += 1
                i -= 1
                break
            i -= 1
    if count<3:
        print(-1)
    else:
        print(ans)
        
