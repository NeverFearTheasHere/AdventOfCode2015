import numpy as np

unitVectorX = np.array([1, 0])
unitVectorY = np.array([0, 1])

def countHousesVisited(directionsInputString):
    currentLocation = np.array([0, 0])
    housesWhichHaveBeenVisited = [currentLocation.copy()]

    directionCharacters = list(directionsInputString)

    while len(directionCharacters) > 0:
        directionCharacter = directionCharacters.pop(0)
        match directionCharacter:
            case '^':
                direction = + unitVectorY
            case '>':
                direction = + unitVectorX
            case '<':
                direction = - unitVectorX
            case 'v':
                direction = - unitVectorY
            case _:
                raise ValueError(f'invalid direction character: {directionCharacter}') 

        currentLocation += direction
        housesWhichHaveBeenVisited.append(currentLocation.copy())

    uniqueHousesWhichHaveBeenVisited = np.unique(np.array(housesWhichHaveBeenVisited), axis = 0)
    return len(uniqueHousesWhichHaveBeenVisited)

if __name__ == '__main__':
    with open('day_03//input.txt') as input:
        numberOfHousesVisited = countHousesVisited(input.read())
    print(f'{numberOfHousesVisited} houses were visited')