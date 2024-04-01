N = int(input())
A = list(map(int, input().split()))

dc = [[A[0], 1]]
ans = 1
print(1)
for i in range(1, N):
    if dc and dc[-1][0]==A[i]:
        dc[-1][1] += 1
        ans += 1
        if dc[-1][1]==dc[-1][0]:
            _, c = dc.pop()
            ans -= c
            # 詰める
            while len(dc)>=2 and dc[-1][0]==dc[-2][0]:
                _, c = dc.pop()
                dc[-1][1] += c
                if dc[-1][1]>=dc[-1][0]:
                    d, c = dc.pop()
                    ans -= d
                    dc.append([d, c-d])
    else:
        dc.append([A[i], 1])
        ans += 1
    print(ans)