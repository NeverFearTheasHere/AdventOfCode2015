def wrappingPaperArea(dimensions):
    areaOfFirstSide = dimensions[0] * dimensions[1]
    areaOfSecondSide = dimensions[0] * dimensions[2]
    areaOfThirdSide = dimensions[1] * dimensions[2]
    areaOfSmallestSide = min((areaOfFirstSide, areaOfSecondSide, areaOfThirdSide))
    return 2 * areaOfFirstSide + 2 * areaOfSecondSide + 2 * areaOfThirdSide + areaOfSmallestSide

def totalWrappingPaperArea(inputFileName):
    dimensionsList = parseInputFile(inputFileName)
    areas = [wrappingPaperArea(dimensions) for dimensions in dimensionsList]
    return sum(areas)

def ribbonLength(dimensions):
    dimensions.sort()
    smallestFacePerimeter = 2 * (dimensions[0] + dimensions[1])
    volume = dimensions[0] * dimensions[1] * dimensions [2]
    return smallestFacePerimeter + volume

def totalRibbonLength(inputFileName):
    dimensionsList = parseInputFile(inputFileName)
    lengths = [ribbonLength(dimensions) for dimensions in dimensionsList]
    return sum(lengths)

def parseInputFile(inputFileName):
    with open(inputFileName) as inputFile:
        lines = inputFile.readlines()
    dimensionsStringsList = [line.replace('\n', '').split('x') for line in lines]
    dimensionsList = [[int(elem) for elem in lst] for lst in dimensionsStringsList]
    return dimensionsList

if __name__ == '__main__':
    wrappingPaperArea = totalWrappingPaperArea('day_02\input.txt')
    print(f'Part 1 - wrapping paper: {wrappingPaperArea} square feet')
    ribbonLength = totalRibbonLength('day_02\input.txt')
    print(f'Part 2 - ribbon length: {ribbonLength} feet')