"""Tの((((連続とは限らない))))部分列！！！！見落としてた～～～～～～"""

N, Q = map(int, input().split())
S = input()

# 事前に11/22文字列をそれぞれ最長になるように列挙しておく
d = []
# d: 最長11/22文字列のlist

i = 0
while i < N:
    l = i
    # lから始まる最長の11/22文字列を求める
    while i < N and S[i] == "1":
        i += 1
    if i == N:
        break

    c = i
    i += 1

    if S[c] != "/":
        continue

    while i < N and S[i] == "2":
        i += 1
    if i == N:
        break

    r = i - 1
    d.append((l, c, r))

print(*d, sep="\n")
