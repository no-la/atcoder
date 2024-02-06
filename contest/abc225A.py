S = input()
n = len(set(list(S)))
if n==1:
    ans = 1
elif n==2:
    ans = 3
elif n==3:
    ans = 6

print(ans)