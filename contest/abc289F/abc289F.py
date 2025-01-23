S = tuple(map(int, input().split()))
T = tuple(map(int, input().split()))
a, b, c, d = map(int, input().split())

# 縦と横で別々に考えていい
# 長方形のサイズ以下ずつなら、長方形に近づいたり、離れたりできる
# なので、操作回数は多分無制限として考えても変わらない、気にしなくていいし、
# 大体の場合は到達できそう
