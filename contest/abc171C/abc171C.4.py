N = int(input())

d = list("abcdefghijklmnopqrstuvwxyz")
k = ""
while N:
    N -= 1
    k += d[N%26]
    N //= 26
    
print(k[::-1])