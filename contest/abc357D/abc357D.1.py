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

N = int(input())
MOD = 998244353

ModInt.MOD = MOD
M = len(str(N))
K = pow(10, M, MOD)
def digit(n):
    return pow(K, 2**n, MOD)

d = [0]*(N.bit_length())
d[0] = ModInt(N)
# d[i]: Nを2^i個つなげたもの

for i in range(1, len(d)):
    d[i] = d[i-1]*digit(i-1)+d[i-1]

# print(*d)

ans = 0
for i in range(N.bit_length()):
    if N & (1<<i):
        ans = ans*digit(i) + d[i]
    
print(ans)
