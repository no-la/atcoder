class ModInt:
    MOD = ...
    def __init__(self, value: int) -> None:
        self.value: int = value%ModInt.MOD
    
    def __add__(self, other) -> "ModInt":
        return (ModInt(self.value + other.value)
                if isinstance(other, ModInt) else
                ModInt(self.value + int(other)))
    
    def __sub__(self, other) -> "ModInt":
        return (ModInt(self.value - other.value)
                if isinstance(other, ModInt) else
                ModInt(self.value - int(other)))
    
    def __mul__(self, other) -> "ModInt":
        return (ModInt(self.value * other.value)
                if isinstance(other, ModInt) else
                ModInt(self.value * int(other)))
    
    def __floordiv__(self, other) -> "ModInt":
        return (ModInt(self.value * pow(other.value, -1, ModInt.MOD))
                if isinstance(other, ModInt) else
                ModInt(self.value * pow(int(other), -1, ModInt.MOD)))
                
    def __pow__(self, other) -> "ModInt":
        return (ModInt(pow(self.value, other.value, ModInt.MOD))
                if isinstance(other, ModInt) else
                ModInt(pow(self.value, int(other), ModInt.MOD)))
    
    def __eq__(self, value: object) -> bool:
        return (self.value == value.value and self.MOD == value.MOD
                if isinstance(value, ModInt) else
                self.value == int(value))
        
    def __radd__(self, other) -> "ModInt":
        return (ModInt(self.value + other.value)
                if isinstance(other, ModInt) else
                ModInt(self.value + int(other)))
    
    def __rsub__(self, other) -> "ModInt":
        return (ModInt(other.value - self.value)
                if isinstance(other, ModInt) else
                ModInt(int(other) - self.value))
    
    def __rmul__(self, other) -> "ModInt":
        return (ModInt(self.value * other.value)
                if isinstance(other, ModInt) else
                ModInt(self.value * int(other)))
    
    def __rfloordiv__(self, other) -> "ModInt":
        return (ModInt(other.value * pow(self.value, -1, ModInt.MOD))
                if isinstance(other, ModInt) else
                ModInt(int(other) * pow(self.value, -1, ModInt.MOD)))
                
    def __rpow__(self, other) -> "ModInt":
        return (ModInt(pow(other.value, self.value, ModInt.MOD))
                if isinstance(other, ModInt) else
                ModInt(pow(int(other), self.value, ModInt.MOD)))
        
    def __str__(self) -> str:
        return str(self.value)

ModInt.MOD = 998244353

K = int(input())
C = list(map(int, input().split()))
N = 26

# 長さK以下
# 各文字iはC[i]個以下

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = ModInt(1)
# dp[i][j]: 1, ..., iの文字を使って長さjの文字列を作る場合の数
for i in range(1, N+1):
    for j in range(1, K+1):
        comb = ModInt(1)
        for k in range(C[i-1]+1):
            if j-k>=0:
                dp[i][j] += dp[i-1][j-k]*comb
            else:
                break
            comb = comb*(j-k)//(k+1)

for d in dp:
    print(*d)

ans = 0
print(sum(dp[N][1:]))
