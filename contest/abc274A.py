A, B = map(int, input().split())

i = B/A
j = 0 if len(str(i))<6 else int(str(i)[5])

if j > 4:
    i += 0.001

ans = str(i)
if len(ans)==1:
    ans += "."
ans = (ans+"00000")[:5]

print(ans)
