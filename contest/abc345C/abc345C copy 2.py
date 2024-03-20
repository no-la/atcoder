S = input()
N = len(S)

count = [0] * 26  # 文字の出現回数を記録する配列

ans = 0
for i in range(N):
    # 文字S[i]より後ろに出現する各文字の数をカウント
    for j in range(ord(S[i]) - ord('a') + 1, 26):
        ans += count[j]
    count[ord(S[i]) - ord('a')] += 1

# 文字列中に同じ文字が複数回出現する場合、最後の文字と一回入れ替えることができる
if any(c > 1 for c in count):
    ans += 1

print(ans)
