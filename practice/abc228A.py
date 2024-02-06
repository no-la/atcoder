S, T, X = map(int, input().split())
if T<S:
    if 0<=X<T or S<=X<24:
        ans = "Yes"
    else:
        ans = "No"
else:
    if S<=X<T:
        ans = "Yes"
    else:
        ans = "No"
print(ans)