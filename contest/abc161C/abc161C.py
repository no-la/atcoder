N, K = map(int, input().split())

x = N
x = N%K
print(min(x, abs(K-x)))