S = input()

ans ="No"
for i in range(0, len(S)):
    if i%2==1 and S[i]=="1":
        break
else:
    ans = "Yes"
print(ans)