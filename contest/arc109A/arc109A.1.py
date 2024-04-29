a, b, x, y = map(int, input().split())

#廊下1回, or 全部廊下
ans = x + min(y, 2*x)*min(abs(b-(a-1)), abs(b-a))
print(ans)
