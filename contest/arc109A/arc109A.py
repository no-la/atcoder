a, b, x, y = map(int, input().split())

#廊下1回, or 全部廊下
print(max(x, min((abs(b-(a-1))*y + x, abs(b-a)*y + x, (2*abs(b-(a-1)) - 1)*x))))
