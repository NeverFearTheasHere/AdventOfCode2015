import numpy as np

unitVectorX = np.array([1, 0])
unitVectorY = np.array([0, 1])

def countHousesVisited(directionsInputString):
    uniqueHousesVisited = np.unique(np.array(housesVisited(directionsInputString)), axis = 0)
    return len(uniqueHousesVisited)

def housesVisited(directionsInputString):
    currentLocation = np.array([0, 0])
    housesVisited = [currentLocation.copy()]

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
        housesVisited.append(currentLocation.copy())

    return housesVisited

def countHousesVisitedWithRoboSanta(directionsInputString):
    santaDirections = directionsInputString[::2]
    roboSantaDirections = directionsInputString[1::2]
    housesVisitedBySanta = housesVisited(santaDirections)
    housesVisitedByRoboSanta = housesVisited(roboSantaDirections)
    uniqueHousesVisited = np.unique(np.array(housesVisitedBySanta + housesVisitedByRoboSanta), axis = 0)
    return len(uniqueHousesVisited)
    
if __name__ == '__main__':
    with open('day_03//input.txt') as input:
        directionsInputString = input.read()
        numberOfHousesVisited = countHousesVisited(directionsInputString)
        numberOfHousesVisitedWithRoboSanta = countHousesVisitedWithRoboSanta(directionsInputString)
    print(f'{numberOfHousesVisited} houses were visited')
    print(f'{numberOfHousesVisitedWithRoboSanta} houses were visited with robo santa')