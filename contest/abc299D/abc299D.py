N = int(input())

l, r = 1, N
while l<r-1: # lは0、rは1
    c = (l+r)//2
    print("?", c)
    s = input()
    if s=="0":
        l = c
    else:
        r = c

print("!", l)
