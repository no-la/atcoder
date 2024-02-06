X = input()

ans, *_ = map(int, X.split("."))
y = int(X[-3])
if y>=5:
    ans += 1
    
print(ans)