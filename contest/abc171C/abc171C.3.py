N = int(input()) - 1 # -1で桁数を揃える

d = list("abcdefghijklmnopqrstuvwxyz")
k = []
while N:
    k.append(N%26)
    N //= 26
    
k = k[::-1]
ans = ""
b = False
for p, i in enumerate(k):
    if p==0 and i==1 and len(k)>=3 and k[1]==0:
        b = True
        k[1] == 26
        continue
    if not b and i==0:
        continue
    b = True
    ans += d[i] if p==len(k)-1 else d[i-1]
print(ans)