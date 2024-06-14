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
T = int(input())

def f(s):
    """１つ前の文字を返す"""
    i = ord(s)
    return chr(i-1)

# 辞書順で一番Sに近い最大の回文を探せばよさそう
# 全てのNの総和は10^6なので、ここで全探索できる
for _ in range(T):
    N = int(input())
    S = input()
    
    # S以下の最大の回文を探せばいい
    offset = ord("A")
    center = 1
    h = (N+1)//2
    tar = S[:h]
    if tar[::-1]>S[-h:]:
        # tarを1下げる
        i = h-1
        while i>=0 and tar[i]=="A":
            i -= 1
        if i>=0:
            tar = tar[:i] + f(tar[i]) + "Z"*((N+1)//2-i-1)
    
    count = ModInt(0)
    for i in range(len(tar)):
        count += (ord(tar[i])-offset)*pow(26, h-i-1, ModInt.MOD)
        
    count += 1 # AA...A(=0)の分
    # print(S, tar, count)

    print(count)
    