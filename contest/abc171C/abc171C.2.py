N = int(input())

d = list("zabcdefghijklmnopqrstuvwxy")
k = ""
while N:
    k += d[N%26]
    N //= 26


print(k[::-1] if not (len(k)>=2 and k[::-1].startswith("az")) else k[::-1][1:])