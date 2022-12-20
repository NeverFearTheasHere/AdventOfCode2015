from day_04 import lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes


#     If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
#     If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

def test_lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes_case1():
    print('abcdef', lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes('abcdef'))
    assert lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes('abcdef') == 609043

def test_lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes_case2():
    assert lowestPositiveDecimalWhoseMD5HashStartsWithFiveZeroes('pqrstuv') == 1048970
