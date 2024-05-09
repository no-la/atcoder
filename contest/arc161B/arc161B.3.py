T = int(input())
for _ in range(T):
    N = int(input())

    ans = 0
    count = 0
    i = N.bit_length()-1
    while i>=0 and count<3:
        if ans+(1<<i)+(2**(2-count)-1)<=N:
            ans += 1<<i
            count += 1
        i -= 1
        # print(N, ans)
    print(ans if count==3 else -1)
        
