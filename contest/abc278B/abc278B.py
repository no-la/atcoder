H, M = map(int, input().split())

h, m = H, M
while True:
    temp_h = h // 10 * 10 + m // 10
    temp_m = h % 10 * 10 + m % 10
    if 0 <= temp_h < 24 and 0 <= temp_m < 60:
        print(h, m)
        break
    m += 1
    if m == 60:
        m = 0
        h += 1
        h %= 24
