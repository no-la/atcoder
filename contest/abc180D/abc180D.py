X, Y, A, B = map(int, input().split())

v = X
ans = 0

# A*v<v+b の間Aを選び
# そうでなくなったらBを選ぶ

# 何回A倍できるかが分かればいい
while A*v<Y and A*v<v+B:
    ans += 1
    v *= A

# 残りはBのみ
ans += max(0, (Y-1-v)//B)

print(ans)
