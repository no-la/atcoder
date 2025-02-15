import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
S = list(map(int, input()))

# 中央値を取ってそこに寄せる？
count = S.count(1)
temp = 0
for i, s in enumerate(S):
    temp += s == 1
    if temp == (count + 1) // 2:
        ci = i
        break

# 全部ciに寄せる
ans = 0

# >>>
temp = 0
for i, s in enumerate(S):
    if i == ci:
        break
    if s == 0:
        ans += temp
    else:
        temp += 1
    # print(temp, ">", ci, "at", (i, s))


# <<<
temp = 0
for i, s in enumerate(S[::-1]):
    if N - i - 1 == ci:
        break
    if s == 0:
        ans += temp
    else:
        temp += 1
    # print(temp, "<", ci, "at", (N - 1 - i, s))

print(ans)
