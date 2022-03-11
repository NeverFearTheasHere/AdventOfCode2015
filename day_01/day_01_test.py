from day_01 import determineFloorLevel

def test_1():
    assert determineFloorLevel('(())') == 0
    assert determineFloorLevel('()()') == 0

def test_2():
    assert determineFloorLevel('(((') == 3
    assert determineFloorLevel('(()(()(') == 3

def test_3():
    assert determineFloorLevel('))(((((') == 3

def test_4():
    assert determineFloorLevel('())') == -1
    assert determineFloorLevel('))(') == -1

def test_5():
    assert determineFloorLevel(')))') == -3
    assert determineFloorLevel(')())())') == -3
