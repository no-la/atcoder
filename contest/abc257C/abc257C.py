N = int(input())
S = input()
W = list(map(int, input().split()))

d = [(W[i], int(S[i])) for i in range(N)]
d.sort()

entire_adult = S.count("1")
entire_chlid = S.count("0")
ans = entire_adult
adult_count = 0
child_count = 0
i = 0
while i < N:
    # X=w+1にしたとき
    w, s = d[i]
    while i < N and d[i][0] == w:
        w, s = d[i]
        if s == 0:
            child_count += 1
        else:
            adult_count += 1
        i += 1

    ans = max(ans, child_count + (entire_adult - adult_count))

print(ans)
