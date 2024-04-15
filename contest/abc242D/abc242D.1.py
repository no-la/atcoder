# https://atcoder.jp/contests/abc242/submissions/52415829
S = input()
Q = int(input())


# 全部の文字が、1->2->4->8->...と増えていく
for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    if t==0:
        print(S[k])
        continue
    elif t>59: # 2^60>10^18
        first = 0
        tar = k
    else:
        tt = 2**t
        first = k//tt
        tar = k%tt
    # print(first, tar)
    s = ord(S[first])-ord("A")
    now = 0
    i = tar
    while i>0:
        now = (now - (1+(i%2)))%3
        i //= 2
    # tar文字目が最初に現れるとき、それはABC[-now]
    delta = tar.bit_length()
    # print("-"*10)
    # print("t", t, "k", k)
    # print("first", first, S[first])
    # print("start with", "ABC"[(-now)%3], "at", delta, "times of", tar)
    print("ABC"[(t-delta+s - now)%3])