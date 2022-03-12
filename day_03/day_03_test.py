from day_03 import countHousesVisited

def test_countHousesVisited_case1():
    assert countHousesVisited('>') == 2

def test_countHousesVisited_case2():
    assert countHousesVisited('^>v<') == 4

def test_countHousesVisited_case3():
    assert countHousesVisited('^v^v^v^v^v') == 2
