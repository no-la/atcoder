Y = int(input())
ans = 365
if Y%4!=0:
    ...
else:
    if Y%100!=0:
        ans = 366
    else:
        if Y%400!=0:
            ...
        else:
            ans = 366
print(ans)
