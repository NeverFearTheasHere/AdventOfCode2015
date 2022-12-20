import re

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

def countNiceStrings(inputFile):
    stringsToTest = inputFile.split('\n')
    return [isNice(s) for s in stringsToTest].count(True)

def isNice(inputString):
    vowels = re.findall(r'a|e|i|o|u', inputString)
    if vowels is None or len(vowels) < 3:
        return False

    doubleLetters = re.search(r'(.)\1', inputString)
    if doubleLetters is None:
        return False

    if re.search(r'ab|cd|pq|xy', inputString) is not None:
        return False
    
    return True


if __name__ == '__main__':
    with open('day_05/input.txt') as input:
        inputFile = input.read()
        numberOfNiceStrings = countNiceStrings(inputFile)
    print(f'{numberOfNiceStrings} strings are nice')