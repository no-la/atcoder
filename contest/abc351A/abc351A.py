A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(max(0, sum(A)+1-sum(B)))
