S = input()
N = len(S)

mod = 2019

# 2019は4桁で、10と互いに素なので、10000個で1周
d = set([str(mod*i) for i in range(1, 10001)])



def f(i):
    if i+4<=N and S[i:i+4] in d:
        r = 4
    elif i+5<=N and S[i:i+5] in d:
        r = 5
    else:
        r = 1
    return r

seen = [False]*N
ans = 0
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    a = f(i)
    if a==1:
        continue
    j = i + a
    c = 1
    ans += c
    while j<N: # この中でseen[j]==Trueにはならない
        seen[j] = True
        a = f(j)
        if a==1:
            break
        j += a
        if j<N:
            c += 1
            ans += c
print(ans)
        
