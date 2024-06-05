from mod_int import ModInt 

def test_add():
    ModInt.MOD = 7
    a = ModInt(0)
    assert (a+1).value == 1
    assert (a+(-1)).value == a.MOD-1
    b = ModInt(10)
    assert (a+b).value == ModInt(10).value

def test_sub():
    ModInt.MOD = 7
    a = ModInt(0)
    assert (a-1).value == a.MOD-1
    assert (a-(-1)).value == 1
    b = ModInt(10)
    assert (a-b).value == ModInt(-10).value

def test_mul():
    ModInt.MOD = 7
    a = ModInt(1)
    assert (a*1).value == 1
    assert (a*(-1)).value == a.MOD-1
    assert (a*2).value == 2
    assert (a*0).value == 0
    assert (a*a.MOD).value == 0
    assert (a*1*2*3*4).value == 24%a.MOD
    b = ModInt(10)
    assert (a*b).value == ModInt(1*10).value

def test_floordiv():
    ModInt.MOD = 7
    a = ModInt(1)
    assert (a//1).value == 1
    assert (a//(-1)).value == a.MOD-1
    assert (a//2).value == 4
    assert ((a+3)//2).value == 2
    assert ((a+4)//3).value == 4
    b = ModInt(10)
    assert (a//b).value == ModInt(1*pow(10, -1, ModInt.MOD)).value

def test_iadd():
    ModInt.MOD = 7
    a = ModInt(1)
    a += 1
    assert a.value == 2
    a += 7
    assert a.value == 2
    a += 5
    assert a.value == 0
    b = ModInt(4)
    a += b
    assert a.value == 4
    assert b.value == 4
    
def test_eq():
    ModInt.MOD = 7
    a = ModInt(1)
    assert a == 1
    assert a == "1"
    assert a != 2
    b = ModInt(1)
    assert a == b
    c = ModInt(2)
    assert a != c

def test_pow():
    ModInt.MOD = 7
    a = ModInt(2)
    b = ModInt(3)
    assert a**2 == 4
    assert a**b == 1

def test_radd():
    ModInt.MOD = 7
    a = ModInt(2)
    assert 3+a == ModInt(5)
    assert 5+a == 0

def test_rsub():
    ModInt.MOD = 7
    a = ModInt(2)
    assert 3-a == ModInt(1)
    assert 5-a == 3

def test_rmul():
    ModInt.MOD = 7
    a = ModInt(2)
    assert 3*a == ModInt(6)
    assert 5*a == 3

def test_rfloordiv():
    ModInt.MOD = 7
    a = ModInt(2)
    assert 3//a == ModInt(12)
    assert 5//a == ModInt(20)

def test_rpow():
    ModInt.MOD = 7
    a = ModInt(2)
    assert 3**a == ModInt(9)
    assert 5**a == ModInt(25)
    
