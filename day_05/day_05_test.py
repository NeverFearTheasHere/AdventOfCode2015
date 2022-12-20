
#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

from day_05 import isNice


def test_isNice_case1():
    assert isNice('ugknbfddgicrmopn')

def test_isNice_case2():
    assert isNice('aaa')

def test_isNice_case3():
    assert not isNice('jchzalrnumimnmhp')

def test_isNice_case4():
    assert not isNice('haegwjzuvuyypxyu')

def test_isNice_case5():
    assert not isNice('dvszwmarrgswjxmb')