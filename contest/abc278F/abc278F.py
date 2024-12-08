N = int(input())
S = [input() for _ in range(N)]


def f(remain, s, turn):
    """
    勝利するプレイヤーを変えす
    remain: 残りの文字列
    s: 直前の文字
    """
    if not remain:
        return turn ^ 1

    for t in list(remain):
        if s != "" and t[0] != s:
            continue
        remain.remove(t)
        res = f(remain, t[-1], turn ^ 1)
        remain.add(t)
        if res == turn:
            return turn
    return turn ^ 1


print(["First", "Second"][f(set(S), "", 0)])
