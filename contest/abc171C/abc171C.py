N = int(input())

d = list("_abcdefghijklmnopqrstuvwxyz") # 1-a, 2-b, ..., 26-z
k = ""
while N:
    k += d[26-(-N%26)] # 1-indexed
    N //= 26

print(k[::-1])