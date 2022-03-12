from day_02 import wrappingPaperArea, totalWrappingPaperArea, ribbonLength, totalRibbonLength

def test_wrappingPaperArea_case1():
    assert wrappingPaperArea([2,3,4]) == 58

def test_wrappingPaperArea_case2():
    assert wrappingPaperArea([1,1,10]) == 43

def test_totalWrappingPaperArea_validInputFile():
    assert totalWrappingPaperArea('day_02//valid_test_input.txt') == 108

def test_ribbonLength_case1():
    assert ribbonLength([2,3,4]) == 34

def test_ribbonLength_case2():
    assert ribbonLength([1,1,10]) == 14

def test_totalRibbonLength_validInputFile():
    assert totalRibbonLength('day_02//valid_test_input.txt') == 53
